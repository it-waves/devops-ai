from PIL import Image
import sys
SRC='/home/claude/academy/lesson23/cloud/'; DST='/home/claude/academy/lesson23/assets/'
TOP=(1420,2,1568,42)
EXTRA={'public_rt':[(578,328,705,350)],'private_rt':[(578,328,705,350)],'map_details':[(1225,282,1345,304)],
 'inst_private_detail':[(255,560,655,602)],'create_workflow':[],'inst_both_list':[],'inst_net_settings':[(284,97,374,117)],
 'inst_terminate_dialog':[],'vpc_delete_dialog2':[],'vpc_deleted2':[]}
def mosaic(im, box, cell=9):
    c=im.crop(box); w,h=c.size
    s=c.resize((max(1,w//cell),max(1,h//cell)),Image.BILINEAR).resize((w,h),Image.NEAREST); im.paste(s,box)
for n,boxes in EXTRA.items():
    im=Image.open(SRC+n+'.jpg').convert('RGB'); mosaic(im,TOP,7)
    for b in boxes: mosaic(im,b,8)
    im.save(DST+n+'.jpg',quality=92)
print('ok')
