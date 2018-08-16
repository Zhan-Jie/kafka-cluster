# 使用说明 #

使用Ansible依次安装JRE、Zookeeper集群、Kafka集群。

使用的软件版本：
- JRE. 8u181
- Zookeeper. 3.4.13
- Kafka. 2.11

## 配置文件 ##

配置文件是config.json，其中各个字段的意义：

- `java_home`. JRE的安装目录；
- `zookeeper_hosts`. 安装zookeeper的主机IP列表；
- `zookeeper_home`. zookeeper的安装目录；
- `zookeeper_data_dir`. zookeeper保存数据的目录；
- `kafka_hosts`. 安装kafka的主机IP列表；
- `kafka_home`. Kafka的安装目录；
- `kafka_log_dir`. Kafka的日志目录。

## 安装 ##

在该项目目录执行命令：`ansible-playbook -i hosts install.yml`。

## 卸载 ##

在该项目目录执行命令：`ansible-playbook -i hosts clean.yml`。

这将会依次停止kafka、zookeeper，并删除它们的安装目录，删除jre安装目录，清除java相关环境变量。
