-- 删除数据库（存在则删除antirumor）
drop database if exists antirumor;

-- 创建数据库
create database antirumor;

-- 使用数据库
use antirumor;

-- 删除表（存在则删除rumor）
drop table if exists rumor;
-- 谣言表
create table rumor (
    id int unsigned auto_increment primary key comment '编号',
    rumor varchar(128) not null comment '谣言',
    truth text not null comment '真相',
    origin varchar(50) comment '辟谣发布平台',
    published_date datetime not null comment '发布时间',
    url varchar(128) comment '辟谣网站的链接'
) comment '谣言表';

-- 删除表（存在则删除tag）
drop table if exists tag;
-- 标签表
create table tag (
    id int unsigned auto_increment primary key comment '编号',
    name varchar(50) not null comment '标签名称'
) comment '标签表';

-- 删除表（存在则删除rumor_tag）
drop table if exists rumor_tag;
-- 谣言标签关联表
create table rumor_tag (
    rumor_id int unsigned not null comment '谣言编号',
    tag_id int unsigned not null comment '标签编号',
    primary key (rumor_id, tag_id),
    constraint fk_rumor_rumor_tag foreign key (rumor_id) references rumor(id) on delete cascade,
    constraint fk_tag_rumor_tag foreign key (tag_id) references tag(id) on delete cascade
) comment '谣言标签关联表';

-- 删除表（存在则删除ask_rumor）
drop table if exists ask_rumor;
-- 用户谣言信息表
create table ask_rumor (
    id int unsigned auto_increment primary key comment '编号',
    rumor varchar(128) not null comment '用户提供的谣言信息',
    num_agree int unsigned default 0 comment '支持的用户数量',
    num_disagree int unsigned default 0 comment '反对的用户数量',
    expert_conclusion text comment '专家意见'
) comment '用户谣言信息表';
