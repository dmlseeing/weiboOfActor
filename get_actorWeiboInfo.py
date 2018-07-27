# !/usr/bin/python3
# -*-coding: utf-8-*-

import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import json
import time

driver = webdriver.Firefox(executable_path='./geckodriver')

def get_actorurl():
    actor_url = open('./actor_url.txt', 'w+')
    with open('./actor_name.csv', 'r+') as f:
        for line in f.readlines():
            name = line.split(',')[1].strip()
            url = 'http://s.weibo.com/weibo/' + name
            driver.get(url)
            try:
                url_homepage = driver.find_element_by_class_name('wb_url').text
                print(name + ' : ' + url_homepage)
                actor_url.write(name + ' : ' + url_homepage)
                actor_url.write('\n')
                driver.close()
            except selenium.common.exceptions.NoSuchElementException:
                # 已手动删除没有微博的演员数据并将名单存入txt文件
                print(name + ' : ' + 'error')
                actor_url.write(name + ' : ' + 'error')
                actor_url.write('\n')
                driver.close()

def get_num_of_follow_fan_weibo():
    with open('./actor_url.txt', 'r+')as f:
        for line in f.readlines():
            url = line.split(':')[1].strip()
            url_hot = 'https:' + url + '?profile_ftype=1&is_all=1#_0'
            try:
                driver.get(url_hot)

                try:
                    time.sleep(5)
                except AttributeError:
                    pass

                try:
                    WebDriverWait(driver, 15, 3).until(
                        lambda browser: browser.find_element_by_class_name("WB_innerwrap"))
                finally:
                    details = driver.find_element_by_class_name('WB_innerwrap')
                    actor_info_1 = details.find_elements_by_class_name('S_txt2')
                    actor_info_2 = details.find_elements_by_class_name('W_f12')
                    if len(actor_info_2) == 0:
                        actor_info_2 = driver.find_elements_by_class_name('W_f14')
                        if len(actor_info_2) == 0:
                            actor_info_2 = driver.find_elements_by_class_name('W_f18')
                            if len(actor_info_2) == 0:
                                actor_info_2 = driver.find_elements_by_class_name('W_f16')
                    movie_info_s = {}
                    for i in range(len(actor_info_1)):
                        movie_info_s[actor_info_1[i].text] = actor_info_2[i].text
                    with open('./data/' + name + '/three_types_num.json', 'w') as f1:
                        json.dump(movie_info_s, f1)
                    driver.close()

            except selenium.common.exceptions.NoSuchElementException:
                print(name + ':error')
                try:
                    time.sleep(20)
                except AttributeError:
                    pass
                driver.close()

def slowdown():
    for i in range(1, 4):  # at most 3 times
        driver.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
        time.sleep(5)
        try:
            # 定位页面底部的换页tab
            driver.find_element_by_xpath('//span[@class="list"]/a[@action-type="feed_list_page_morelist"]')
            break  # 如果没抛出异常就说明找到了底部标志，跳出循环
        except:
            pass  # 抛出异常说明没找到底部标志，继续向下滑动

def get_totalinfo_of_firstpage():
    with open('./actor_url.txt', 'r+')as f:
        for line in f.readlines():
            url = line.split(':')[1].strip()
            url_hot = 'https:' + url + '?profile_ftype=1&is_all=1#_0'
            try:
                driver.get(url_hot)
                for i in range(1, 4):
                    slowdown()  # 下滑的函数
                    driver.execute_script("window.scrollTo(100000,document.body.scrollHeight);")

                try:
                    time.sleep(5)
                except AttributeError:
                    pass

                try:
                    WebDriverWait(driver, 15, 3).until(
                        lambda browser: browser.find_element_by_class_name("WB_innerwrap"))
                finally:
                    content = driver.find_element_by_xpath('//div[@class = "WB_feed WB_feed_v3 WB_feed_v4"]')
                    time = content.find_elements_by_xpath('//div[@class = "WB_from S_txt2"]')
                    weibo = content.find_elements_by_xpath('//div[@class = "WB_text W_f14"]')
                    with open('./data/' + name + '/time_weibo.txt', 'w') as f1:
                        newlines = '\n'
                        for i in range(len(weibo)):
                            f1.writelines(time[i].text)
                            f1.writelines(newlines)
                            f1.writelines(weibo[i].text)
                            f1.writelines(newlines)
                            f1.writelines(newlines)
                    print(name + ':success')
                    driver.close()

            except selenium.common.exceptions.NoSuchElementException:
                print(name + ':error')
                try:
                    time.sleep(20)
                except AttributeError:
                    pass
                driver.close()

def get_basicinfo():
    with open('./basic_url.txt', 'r')as f:
        for line in f.readlines():
            url = line.split(':')[1].strip() + ':' + line.split(':')[2].strip()
            name = line.split(':')[0].strip()
            info = open('./data/' + name + '/basic_information.txt', 'w')
            driver.get(url)
            time.sleep(20)
            content = driver.find_elements_by_class_name('WB_frame_c')
            print(len(content))
            for index in range(len(content)):
                try:
                    print(content[index].text)
                    print('\n')
                    info.write(content[index].text)
                except IndexError:
                    print('IndexError')
    driver.close()

def get_totalnumof_forward_like():
    with open('./actor_url.txt', 'r+')as f:
        for line in f.readlines():
            name = line.split(':')[0].strip()
            url = line.split(':')[1].strip()
            file = open('./runForData/' + name + '.txt', 'w')
            url_hot = 'https:' + url + '?profile_ftype=1&is_all=1#_0'
            driver.get(url_hot)
            time.sleep(30)
            content = driver.find_elements_by_xpath('//ul[@class = "WB_row_line WB_row_r4 clearfix S_line2"]')
            for i in range(len(content)):
                print(i)
                print(content[i].text)
                file.write(content[i].text)
                file.write('\n')

            file1 = open('./runForData/' + name + '_data.txt', 'w')
            i = 0
            with open('./runForData/' + name + '.txt', 'r')as f1:
                for line1 in f1.readlines():
                    file1.write(line1.strip())
                    i = i + 1
                    if (i == 4):
                        i = 0
                        file1.write('\n')

            numOfForward = 0
            numOfLike = 0
            with open('./runForData/' + name + '_data.txt', 'r')as f2:
                for line2 in f2.readlines():
                    data = line2.split('')[1].strip()
                    num = data.split('')
                    try:
                        numOfForward += int(num[0])
                        numOfLike += int(num[1].split('ñ')[1].strip())
                    except ValueError:
                        pass
            info = name + ' : { 转发数:' + str(numOfForward) + ' ; 点赞数:' + str(numOfLike) + ' }'
            print(info)
        driver.close()

if __name__ == '__main__':
    # get_actorurl()
    # get_num_of_follow_fan_weibo()
    # get_totalinfo_of_firstpage()
    # get_basicinfo()
    # get_totalnumof_forward_like()
    print('The task is completely finished!')