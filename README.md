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
[TestObj.m]
ERROR => POS [16:1] : NSString 要用 copy 不能用 strong  -5.0
SUGGEST => POS [20:1] : 是否没有足够的program mark宏将函数分组  -10.0
WARN => POS [26:1] : 函数头前空格个数错误  -0.5
WARN => POS [26:12] : { 前缺少空格  -0.5
WARN => POS [31:1] : 函数头前空格个数错误  -0.5
WARN => POS [31:12] : { 前缺少空格  -0.5
WARN => POS [36:14] : 函数参数过多  -0.5
WARN => POS [39:26] : { 前缺少空格  -0.5
WARN => POS [44:23] : *号前缺少空格  -0.5
ERROR => POS [56:9] : 不要直接使用 addObject  -3.0
ERROR => POS [57:8] : 不要直接使用 setObject: forKey:  -3.0
ERROR => POS [58:8] : 不要直接使用 setObject: forKey:  -3.0
ERROR => POS [60:9] : 不要直接使用 removeObjectForKey  -3.0
ERROR => POS [61:3] : 不要直接使用 dict[key] = value  -3.0
ERROR => POS [62:3] : 不要直接使用 dict[key] = value  -3.0
ERROR => POS [64:3] : 不要直接使用 dict[key] = value  -3.0
ERROR => POS [65:1] : 不要直接使用 array[index] 如果是 C 数组，请忽略  -3.0
WARN => POS [68:7] : =号前缺少空格  -0.5
WARN => POS [69:8] : =号后缺少空格  -0.5
WARN => POS [70:7] : =号前缺少空格  -0.5
WARN => POS [70:7] : =号后缺少空格  -0.5
WARN => POS [71:6] : ==前缺少空格  -0.5
WARN => POS [71:7] : ==后缺少空格  -0.5
WARN => POS [73:14] : ==后缺少空格  -0.5
WARN => POS [75:13] : ==前缺少空格  -0.5
WARN => POS [79:12] : { 前缺少空格  -0.5
WARN => POS [79:22] : { 前缺少空格  -0.5
WARN => POS [86:1] : 逻辑分支内为空，请加入 do nothing 注释  -1.0
WARN => POS [90:1] : 函数头前空格个数错误  -0.5
WARN => POS [91:1] : 逻辑分支内为空，请加入 do nothing 注释  -1.0
WARN => POS [95:1] : 函数头前空格个数错误  -0.5
WARN => POS [96:1] : 逻辑分支内为空，请加入 do nothing 注释  -1.0
WARN => POS [100:1] : 函数头前空格个数错误  -0.5
WARN => POS [101:1] : 逻辑分支内为空，请加入 do nothing 注释  -1.0
WARN => POS [105:1] : 函数头前空格个数错误  -0.5
WARN => POS [106:1] : 逻辑分支内为空，请加入 do nothing 注释  -1.0
WARN => POS [111:1] : 函数过长，超过100行  -20.0
WARN => POS [114:5] : *号前缺少空格  -0.5
得分 25.0
[TestObj.h]
ERROR => POS [15:1] : NSString 要用 copy 不能用 strong  -5.0
ERROR => POS [18:1] : 函数缺少注释  -5.0
ERROR => POS [20:1] : 函数缺少注释  -5.0
WARN => POS [20:14] : 函数参数过多  -0.5
得分 84.5
DONE !!!
```

