//
//  TestObj.h
//  aaaa
//
//  Created by icefire_wang on 2018/10/26.
//  Copyright © 2018 wangjian. All rights reserved.
//

#import <Foundation/Foundation.h>



@interface TestObj : NSObject

@property (nonatomic,strong) NSString *string; //  NG string use strong


- (void)func1; // NG func need comment

@end


