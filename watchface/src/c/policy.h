#pragma once
#include "digits.h"
static inline int uses_24(int format,int watch_24) {return format==2 || (format==0 && watch_24);}
static inline int display_hour(int hour,int format,int watch_24) {return uses_24(format,watch_24)?hour:(hour%12?hour%12:12);}
static inline int battery_bars(int percent) {return percent<=0?0:(percent+24)/25;}
static inline int battery_group_left(int text_width) {return (200-(48+12+text_width))/2;}
static const int DIGIT_X[4]={20,58,108,146};
static inline void clock_bounds(int hour,int minute,int *left,int *right) {
 int values[4]={hour/10,hour%10,minute/10,minute%10};*left=96;*right=102;
 for(int i=0;i<4;i++) {
  int a=DIGIT_X[i]+DIGIT_LEFT[values[i]],b=DIGIT_X[i]+DIGIT_RIGHT[values[i]];
  if(a<*left) *left=a;
  if(b>*right) *right=b;
 }
}
static inline int clock_offset(int hour,int minute) {int a,b;clock_bounds(hour,minute,&a,&b);return (199-a-b)/2;}
