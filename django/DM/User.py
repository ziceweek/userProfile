__author__ = 'zice'
# coding:utf-8
import os
import bs4
from bs4 import BeautifulSoup


class UserBaseInfo:
    id = 1912037383
    screenName = '广外图书馆'
    name = '广外图书馆'
    province = '44'
    city = 1
    location = '广东 广州'
    description = ''
    url = 'http://lib.gdufs.edu.cn'
    profileImageUrl = 'http://tp4.sinaimg.cn/1912037383/50/1299747450/1'
    userDomain = 'gdufslib'
    gender = 'm'
    followersCount=0
    friendsCount=0
    statusesCount=0
    favouritesCount=1757
    createdAt = 'Wed Jan 05 10:09:54 CST 2011'
    following = True  # (原始数据中是true)
    verified = True  # (原始数据中是true)
    verifiedType = 4
    allowAllActMsg = False  # (原始数据中是false)
    allowAllComment = True  # (原始数据中是true)
    followMe = False  # (原始数据中是false)
    avatarLarge = 'http://tp4.sinaimg.cn/1912037383/180/1299747450/1'
    onlineStatus = 1
    status = Status()
    biFollowersCount = 448
    remark = 0
    lang = 'zh-cn'
    verifiedReason = 0
    weihao = 0
    statusId = 0
    WeiboList = []

    def __int__(self,):
        return 0

    def setWeiboList(self, xmlweibolist):
        for line in xmlweibolist:
        soup = BeautifulSoup(line)
        <weibo>
            <mid>3772762696592448</mid>
            <uid>1912037383</uid>
            <ruid>11111111</ruid>
            <text>置顶 #文化景观行##广外图书馆#“天堂应该是图书馆的模样” ，对于广外人，图书馆是永远的挚友，是广外人的文化传承。在广外即将迎来建校五十周年之际，广外新闻网、《广外校报》策划推出“广外文化景观行”系列报道，让我们走进“文化景观行”的第八站——广外图书馆。详情O网页链接[太开心]</text>#
            <originText></originText>
            <weiboDate>1414980184000</weiboDate>
            <commentCount>4</commentCount>
            <repostCount>8</repostCount>
            <zanCount>0</zanCount>
            <source></source>
            <url>http://weibo.com/1912037383/BuwTbrEZO</url>
        </weibo>
        soup.uid
        print soup.text
        return 0
class Status:
    user = 0
    idstr=0
    createdAt = 0
    id=0
    text=''
    source = 0
    favorited = False
    truncated = False
    inReplyToStatusId = -1
    inReplyToUserId = -1
    inReplyToScreenName = 0  # 原文中是空
    thumbnailPic=0  # 原文中为空
    bmiddlePic = 0  # 同上
    originalPic = 0
    retweetedStatus = 0
    geo = 0
    latitude = -1.0
    longitude = -1.0
    repostsCount = 0
    commentsCount = 0
    mid = 0
    annotations = 0
    mlevel = 0
    visible = 0

    def __int__(self):
        return 0


