#include <Microduino_Key.h>
#include"userDef.h"
#include"colorLed.h"
#include"motor.h"



void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.setBrightness(BRIGHT_MAX);
  keyMic.begin(INPUT);
  MotorLeft.begin();
  MotorRight.begin();
#if DEBUG
  Serial.println("**************START************");
#endif
}

void loop() {
#if DEBUG
  Serial.print("MIC Val:");
  Serial.println(analogRead(PIN_MIC));
#endif
  if (keyMic.readEvent(VOICE_MIN, VOICE_MAX) == SHORT_PRESS)  //如果声音传感器检测到了声音，风车和LED灯将会启动。
  {
    uint32_t motorTimer = millis();
    while (millis() - motorTimer < TIME_RUN)            //在检测到声音的10秒钟以内
    {
      motorRun(MOTOR_SPEED_MAX, MOTOR_SPEED_MAX);       //启动电机。
      ledRainbow(10);                                   //LED开始变换彩虹颜色。
    }
  }
  else                                   //检测到声音10秒钟以后
  {
    motorFree();                        //关掉电机。
    setAllColor(COLOR_NONE);              //关掉LED灯。
  }
}
