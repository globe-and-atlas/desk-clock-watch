from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[1]

def test_time_centering_and_battery(tmp_path):
    source='''#include <assert.h>
#include "policy.h"
int main(void) {
 for(int hour=0;hour<24;hour++) {
  assert(display_hour(hour,2,0)==hour);
  assert(display_hour(hour,0,1)==hour);
  assert(display_hour(hour,1,1)==(hour%12?hour%12:12));
  assert(display_hour(hour,0,0)==(hour%12?hour%12:12));
  for(int minute=0;minute<60;minute++) {
   int a,b;clock_bounds(hour,minute,&a,&b);int offset=clock_offset(hour,minute);
   assert(a+offset>=20 && b+offset<180);
   assert(a+b+2*offset>=198 && a+b+2*offset<=200);
  }
 }
 for(int percent=0;percent<=100;percent++) {
  int bars=battery_bars(percent);assert(bars>=0 && bars<=4);
  if(percent==0) assert(bars==0);
  if(percent==100) assert(bars==4);
 }
 for(int width=12;width<=60;width++) {
  int left=battery_group_left(width);assert(left>=0 && left+60+width<=200);
  assert(left*2+60+width>=199 && left*2+60+width<=200);
 }
 return 0;
}'''
    (tmp_path/'test.c').write_text(source)
    subprocess.run(['cc','-Wall','-Werror','-I',str(ROOT/'watchface/src/c'),str(tmp_path/'test.c'),'-o',str(tmp_path/'test')],check=True)
    subprocess.run([str(tmp_path/'test')],check=True)

def test_rounded_masks_have_open_counters():
    import importlib.util
    spec=importlib.util.spec_from_file_location('generate_digits',ROOT/'execution/generate_digits.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    for digit in range(10):
        mask=module.glyph_mask(digit)
        assert mask.size==(34,64)
        assert mask.getbbox()[1]<=1
        assert mask.getbbox()[3]>=63
    for digit in [0,6,8,9]:
        mask=module.glyph_mask(digit)
        # Numeral counters retain background near the center of their bowls.
        row=18 if digit in [8,9] else 45 if digit==6 else 32
        assert mask.getpixel((17,row))==0
