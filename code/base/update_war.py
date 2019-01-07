＃-*-coding:utf-8-*-
#import subprocess
import os


class BaseUpdateProject:
    def backup(self):
        pass

    def deploy(self):
        pass

    def rollback(self):
        pass

    def handle_update(self):
        in_project = True
        while in_project:
            print("1. backup")
            print("2. deploy")
            print("3. rollback")
            print("4. 返回上一层")
            print("请输入序号：")

            order = input()
            if order == '4':
                in_project = False
                break

            if order == '1':
                self.backup()
            elif order == '2':
                self.deploy()
            elif order == '3':
                self.rollback()
            else:
                print("您输入的数字有误")


class UpdateLiveStream(BaseUpdateProject):
    NAME = '1'

    def backup(self):
        print("live backup")
        print(os.system('dir'))

    def deploy(self):
        print("live deploy")

    def rollback(self):
        print("live rollback")


class UpdateCometd(BaseUpdateProject):
    NAME = '2'

    def backup(self):
        print("cometd deploy")
        print(os.system('dir'))

    def deploy(self):
        print("cometd deploy")

    def rollback(self):
        print("cometd rollback")


class UpdateBackend(BaseUpdateProject):
    NAME = '3'

    def backup(self):
        print("backend deploy")
        print(os.system()('dir'))

    def deploy(self):
        print("backend deploy")

    def rollback(self):
        print("backend rollback")


class ProjectFactory:

    @staticmethod
    def get_project(name):
        projects_ = {
            "live": UpdateLiveStream(),
            "cometd": UpdateCometd(),
            "backend": UpdateBackend()
        }
        return projects_[name]


running = True
factor = ProjectFactory()
while running:
    print("live")
    print("cometd")
    print("backend")
    print("quit")
    print("请输入准备操作项目的名称：")
    number = input()
    if number == 'quit':
        running = False
        break

    try:
        updateProject = factor.get_project(number)
        updateProject.handle_update()
    except:
        print("我不认识" + number + "!!")

