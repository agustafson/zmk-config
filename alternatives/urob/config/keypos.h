/* TOTEM: native 38-position matrix-transform order. */
#pragma once

#define LT0 4
#define LT1 3
#define LT2 2
#define LT3 1
#define LT4 0
#define RT0 5
#define RT1 6
#define RT2 7
#define RT3 8
#define RT4 9
#define LM0 14
#define LM1 13
#define LM2 12
#define LM3 11
#define LM4 10
#define RM0 15
#define RM1 16
#define RM2 17
#define RM3 18
#define RM4 19
#define LB0 25
#define LB1 24
#define LB2 23
#define LB3 22
#define LB4 21
#define RB0 26
#define RB1 27
#define RB2 28
#define RB3 29
#define RB4 30
#define LH0 34
#define LH1 33
#define LH2 32
#define RH0 35
#define RH1 36
#define RH2 37
#define LX 20
#define RX 31

#define KEYS_L LT0 LT1 LT2 LT3 LT4 LM0 LM1 LM2 LM3 LM4 LB0 LB1 LB2 LB3 LB4 LX
#define KEYS_R RT0 RT1 RT2 RT3 RT4 RM0 RM1 RM2 RM3 RM4 RB0 RB1 RB2 RB3 RB4 RX
#define THUMBS_L LH0 LH1 LH2
#define THUMBS_R RH0 RH1 RH2
#define THUMBS THUMBS_L THUMBS_R
