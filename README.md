# OCStyleMaster
一个检查Objective-C 代码规范的工具 **Python3** 编写

## 安装
```
$ pip install ocstylemaster
```



## 使用
```
$occ -f (the path to your .m of .h file or folder)
```



## 效果

.h File

```
//
//  TestObj.h
//  Test
//
//  Created by icefire_wang on 2018/10/26.
//  Copyright © 2018 icefire_wang. All rights reserved.
//

#import <Foundation/Foundation.h>



@interface TestObj : NSObject

@property (nonatomic,strong) NSString *string; //  NG string use strong


- (void)func1; // NG func need comment

@end

```



.m File:

```
//
//  TestObj.m
//  aaaa
//
//  Created by icefire_wang on 2018/10/26.
//  Copyright © 2018 icefire_wang. All rights reserved.
//

#import "TestObj.h"

@implementation TestObj

/*
        test comment*
*/

-(void)func1{
  // 函数头，减号后没有空格
  // func header lack space
}

+(void)func2{
  // 函数头，减号后没有空格
  
  // func header lack space
}
//
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
  int b= 1;
  int c =1;
  int d=1;
  if (a==1) { //NG == 号前后没有空格

  } else if(a ==2) { // NG

  } else if (a== 3) { // NG

  }

  if(b == 1){ // NG  "{" 前无空格

  }

}

- (void)placeholderFunc1
{

}

-(void)placeholderFunc2 // NG need blank after "-"
{

}

-(void)placeholderFunc3 // NG need blank after "-"
{

}

-(void)placeholderFunc4 // NG need blank after "-"
{

}

-(void)placeholderFunc5 // NG need blank after "-"
{

}


- (void)aVeryLongFunc // NG need blank after "-"
{ // NG func to long
  NSLog(@"1");
    /*
        test comment2
    */
  NSLog(@"1");
  .
  .
  .
  .
  .
  NSLog(@"1");
}


@end

```



#### 检查结果

```
testMain.py .[TestObj.m] Function Count : 11; Average Function Line Count 14.82
ErrorType.suggest => [11:1] : 是否没有足够的program mark宏将函数分组
ErrorType.warn => [17:1] : 函数头前空格个数错误
ErrorType.warn => [17:12] : { 前缺少空格
ErrorType.warn => [22:1] : 函数头前空格个数错误
ErrorType.warn => [22:12] : { 前缺少空格
ErrorType.suggest => [28:1] : 参数过多
ErrorType.warn => [31:26] : { 前缺少空格
ErrorType.warn => [36:23] : *号前缺少空格
ErrorType.warn => [48:9] : 不要直接使用 addObject
ErrorType.warn => [49:8] : 不要直接使用 setObject: forKey:
ErrorType.warn => [50:8] : 不要直接使用 setObject: forKey:
ErrorType.warn => [52:9] : 不要直接使用 removeObjectForKey
ErrorType.warn => [53:3] : 不要直接使用 dict[key] = value
ErrorType.warn => [54:3] : 不要直接使用 dict[key] = value
ErrorType.warn => [56:3] : 不要直接使用 dict[key] = value
ErrorType.warn => [57:1] : 不要直接使用 array[index] 如果是 C 数组，请忽略
ErrorType.warn => [60:7] : =号前缺少空格
ErrorType.warn => [61:8] : =号后缺少空格
ErrorType.warn => [62:7] : =号前缺少空格
ErrorType.warn => [62:7] : =号后缺少空格
ErrorType.warn => [63:6] : ==前缺少空格
ErrorType.warn => [63:7] : ==后缺少空格
ErrorType.warn => [65:14] : ==后缺少空格
ErrorType.warn => [67:13] : ==前缺少空格
ErrorType.warn => [71:12] : { 前缺少空格
ErrorType.warn => [71:22] : { 前缺少空格
ErrorType.warn => [78:1] : 逻辑分支内为空，请加入 do nothing 注释
ErrorType.warn => [82:1] : 函数头前空格个数错误
ErrorType.warn => [83:1] : 逻辑分支内为空，请加入 do nothing 注释
ErrorType.warn => [87:1] : 函数头前空格个数错误
ErrorType.warn => [88:1] : 逻辑分支内为空，请加入 do nothing 注释
ErrorType.warn => [92:1] : 函数头前空格个数错误
ErrorType.warn => [93:1] : 逻辑分支内为空，请加入 do nothing 注释
ErrorType.warn => [97:1] : 函数头前空格个数错误
ErrorType.warn => [98:1] : 逻辑分支内为空，请加入 do nothing 注释
ErrorType.warn => [103:1] : 函数过长，超过100行
ErrorType.warn => [106:5] : *号前缺少空格
[TestObj.h]
ErrorType.warn => [15:1] : NSString 要用 copy 不能用 strong
ErrorType.error => [18:1] : 函数缺少注释
DONE !!!
```

