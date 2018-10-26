//
//  TestObj.m
//  aaaa
//
//  Created by icefire_wang on 2018/10/26.
//  Copyright © 2018 wangjian. All rights reserved.
//

#import "TestObj.h"

@implementation TestObj



-(void)func1{
  // 函数头，减号后没有空格
  // func header lack space
}

+(void)func2{
  // 函数头，减号后没有空格
  // func header lack space
}

+ (void)func3:(NSString *)a
        arg2:(NSString *)b
        arg3:(NSString *)c
        arg4:(NSString *)d{
  // 太多参数
  // too many args
}

+ (void)func4:(NSString*)a
{
  // NSString 后需要空格
  // need space after NSString
}

- (void)arrayDictionaryTest
{
  NSMutableDictionary *dict = [NSMutableDictionary dictionary];
  NSMutableArray *array = [NSMutableArray array];
  NSString *key = @"key";
  NSString *value = @"value";
  [array addObject:value];
  [dict setObject:value forKey:@"a"];  // NG
  [dict setObject:@"abc" forKey:value]; // NG
  [dict setObject:@1 forKey:@2];    // OK
  [dict removeObjectForKey:@"unknowKey"];
  dict[@"key"] = value;   // NG
  dict[key] = @"value"; // NG
  dict[@"key"] = @"value"; // OK
  array[0] = @"1";  //NG
  NSString *getValue = array[0]; //NG
  
  int a = 1;
  if (a==1){ //NG == 号前后没有空格
    
  }else if(a ==2){ // NG
    
  }else if (a== 3){ // NG
    
  }
  
}

- (void)placeholderFunc1
{
  
}

-(void)placeholderFunc2
{
  
}

-(void)placeholderFunc3
{
  
}

-(void)placeholderFunc4
{
  
}

-(void)placeholderFunc5
{
  
}


- (void)aVeryLongFunc
{ // NG func to long
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
  NSLog(@"1");
}


@end
