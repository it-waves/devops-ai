# Jenkins lab setup (sandbox) - MC17

- War: Jenkins 2.580.2 LTS, from repo.jenkins-ci.org (Maven, JFrog S3 host allowed):
  /releases/org/jenkins-ci/main/jenkins-war/2.580.2/jenkins-war-2.580.2.war -> /home/claude/jenkins-lab/jenkins.war
- get.jenkins.io redirects to rotating mirrors that are NOT allowed -> plugin binaries cannot come from the real update site.
- Workaround (disclose in "Honest notes"): /home/claude/jenkins-lab/mkuc.py rewrites update-center.json (from
  https://updates.jenkins.io/dynamic-stable-2.580.2/update-center.json) so every plugin url -> repo.jenkins-ci.org Maven path (from gav).
  Served on 127.0.0.1:8081 (cd site; python3 -m http.server 8081). Jenkins home has hudson.model.UpdateCenter.xml pointing there,
  and Jenkins runs with -Dhudson.model.DownloadService.noSignatureCheck=true. The UI is identical to the real update center.
- L154 home: /home/claude/jenkins-lab/home154 (admin / devops-lab, 91 suggested plugins, wizard skipped); start with run154.sh.
- Plugins installed with inst.sh (POST /pluginManager/installNecessaryPlugins). Restart once after install.
- UI recording: Xvfb :97 1920x1080 + google-chrome (scale 1.25, window 1536x864) + common/cursorfx.py + ffmpeg x11grab (see lesson138/record.py).
- L155 needs a FRESH home (real unlock wizard): create new home with the UpdateCenter.xml only (no init.groovy, no runSetupWizard=false).
- Disk is tight (~1.7 GB free): home154 is ~250 MB.
