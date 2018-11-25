//
//  RootViewController.m
//  VPNOne
//
//  Created by icefire_wang on 2018/9/16.
//  Copyright © 2018年 wangjian. All rights reserved.
//

#import "RootViewController.h"
#import "RootViewModel.h"
#import "VPNManager.h"
@interface RootViewController ()<UITableViewDelegate,UITableViewDataSource>

@property (nonatomic,strong) UITableView *tableView;
@property (nonatomic,strong) RootViewModel *model;

@property (nonatomic,strong) NSArray *dataArray;

@end

@implementation RootViewController

-(instancetype)init{
  self = [super init];
  if (self) {
    self.model = [[RootViewModel alloc] init];
  }
  return self;
}
- (void)viewDidLoad {
    [super viewDidLoad];
    self.dataArray = @[
                       @[
                         @[@"Connect VPN",@"onConnectVPN"],
                          @[@"URL Connection",@"onURLConnection"],
                        ]
                       ];
  
  [self.view addSubview:self.tableView];
  [self.tableView mas_makeConstraints:^(MASConstraintMaker *make) {
    make.edges.equalTo(self.view);
  }];
  
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


-(UITableView*)tableView
{
  if (_tableView == nil) {
    _tableView = [[UITableView alloc] initWithFrame:CGRectZero style:UITableViewStyleGrouped];
    _tableView.dataSource = self;
    _tableView.delegate = self;
    [_tableView setSeparatorStyle:UITableViewCellSeparatorStyleNone];
  }
  return _tableView;
}


#pragma mark - tableview delegate
-(NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
  return self.dataArray.count;
}

-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
  NSArray *array = [self.dataArray objectAtIndex:section];
  return array.count;
}

-(UITableViewCell*)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
  UITableViewCell *cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"default"];
  NSArray *data = self.dataArray[indexPath.section][indexPath.row];
  cell.textLabel.text = data[0];
  return cell;
}


-(CGFloat)tableView:(UITableView *)tableView heightForHeaderInSection:(NSInteger)section
{
  return CGFLOAT_MIN;
}

-(CGFloat)tableView:(UITableView *)tableView heightForFooterInSection:(NSInteger)section
{
  return CGFLOAT_MIN;
}

-(CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
  return 44.f;
}

-(BOOL)tableView:(UITableView *)tableView shouldHighlightRowAtIndexPath:(NSIndexPath *)indexPath
{
  return YES;
}

-(void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
  [tableView deselectRowAtIndexPath:indexPath animated:YES];
  NSArray *data = self.dataArray[indexPath.section][indexPath.row];
  [self performSelector:NSSelectorFromString(data[1]) withObject:nil afterDelay:0];
}

#pragma mark - Action
-(void)onURLConnection
{
  NSString *url = @"http://www.baidu.com";
  [self.model urlConnectionRequest:url];
}

-(void)onConnectVPN
{
  [[VPNManager share] connectVPN];
}

+(instancetype)share
{
  static id ret = nil;
  static dispatch_once_t once;
  
  dispatch_once(&once, ^{
    ret = [[self.class alloc] init];
  });
  return ret;
}
@end
