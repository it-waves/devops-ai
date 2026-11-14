# usage: mkrepo.sh DIR  -- writes a tiny file-based Maven repository with libs liba, libb, util 1.0/2.0
R=$1; G=com/cloudcart/lib
mk() { # artifact version depart depver
  a=$1; v=$2; d=$R/$G/$a/$v; mkdir -p $d
  { echo '<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>'
    echo "<groupId>com.cloudcart.lib</groupId><artifactId>$a</artifactId><version>$v</version>"
    if [ -n "$3" ]; then echo "<dependencies><dependency><groupId>com.cloudcart.lib</groupId><artifactId>$3</artifactId><version>$4</version></dependency></dependencies>"; fi
    echo '</project>'; } > $d/$a-$v.pom
  w=$(mktemp -d); mkdir -p $w/cloudcart/lib
  case "$a" in
   util) cat > $w/cloudcart/lib/Util.java <<EOF
package cloudcart.lib;
public class Util {
    public static String version() { return "$v"; }
$( [ "$v" = 2.0 ] && echo '    public static String shout(String s) { return s.toUpperCase() + "!"; }' )
}
EOF
   ;;
   liba) cat > $w/cloudcart/lib/LibA.java <<EOF
package cloudcart.lib;
public class LibA { public static String name() { return "liba"; } }
EOF
   ;;
   libb) cat > $w/cloudcart/lib/LibB.java <<EOF
package cloudcart.lib;
public class LibB { public static String name() { return "libb"; } }
EOF
   ;;
  esac
  ( cd $w && javac --release 21 -d out cloudcart/lib/*.java && jar cf $d/$a-$v.jar -C out . )
  rm -rf $w
}
mk util 1.0; mk util 2.0; mk liba 1.0 util 1.0; mk libb 1.0 util 2.0
