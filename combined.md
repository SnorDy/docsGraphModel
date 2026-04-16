---
entry_url: https://eventmesh.apache.org/docs/introduction
page_count: 38
asset_count: 39
---
# Introduction to EventMesh
## Navigation
- Introduction to EventMesh (https://eventmesh.apache.org/docs/introduction)
- [Development Roadmap](#roadmap)
- [Installation and Deployment](#instruction-store)
  - [Event Store](#instruction-store)
  - [Event Store with Docker](#instruction-store-with-docker)
  - [EventMesh Runtime Quick Start](#instruction-runtime)
  - [EventMesh Runtime with Docker](#instruction-runtime-with-docker)
  - [Run Java SDK Demo](#instruction-demo)
  - [Integrate EventMesh with K8S](#instruction-operator)
  - [Frequently Asked Questions](#instruction-faq)
- [Design Document](#design-document-event-handling-and-integration-runtime-protocol)
  - [Event Handling and Integration](#design-document-event-handling-and-integration-runtime-protocol)
    - [EventMesh Runtime Protocol](#design-document-event-handling-and-integration-runtime-protocol)
    - [HTTPS](#design-document-event-handling-and-integration-https)
    - [CloudEvents Integration](#design-document-event-handling-and-integration-cloudevents)
    - [Event Bridge](#design-document-event-handling-and-integration-event-bridge)
    - [Use Webhook to subscribe events](#design-document-event-handling-and-integration-webhook)
    - [EventMesh Workflow](#design-document-event-handling-and-integration-workflow)
  - [Observability](#design-document-observability-metrics-export)
    - [EventMesh Metrics (OpenTelemetry and Prometheus)](#design-document-observability-metrics-export)
    - [Distributed Tracing](#design-document-observability-tracing)
    - [Observe Metrics with Prometheus](#design-document-observability-prometheus)
    - [Collect Trace with Zipkin](#design-document-observability-zipkin)
    - [Collect Trace with Jaeger](#design-document-observability-jaeger)
  - [Connect](#design-document-connect-connectors)
    - [Connectors](#design-document-connect-connectors)
    - [RabbitMQ](#design-document-connect-rabbitmq-connector)
    - [HTTP](#design-document-connect-http-connector)
    - [Redis](#design-document-connect-redis-connector)
    - [MongoDB](#design-document-connect-mongodb-connector)
    - [Knative](#design-document-connect-knative-connector)
    - [Feishu/Lark](#design-document-connect-lark-connector)
    - [DingTalk](#design-document-connect-dingtalk-connector)
    - [WeCom](#design-document-connect-wecom-connector)
    - [Slack](#design-document-connect-slack-connector)
  - [EventMesh Schema Registry (OpenSchema)](#design-document-schema-registry)
  - [Service Provider Interface](#design-document-spi)
  - [EventMesh Stream](#design-document-stream)
- [EventMesh SDK for Java](#sdk-java-intro)
  - [Installation](#sdk-java-intro)
  - [HTTP Protocol](#sdk-java-http)
  - [TCP Protocol](#sdk-java-tcp)
  - [gRPC Protocol](#sdk-java-grpc)
- [Upgrade Guide](#upgrade-guide-upgrade-guide)
  - [EventMesh Upgrade Guide](#upgrade-guide-upgrade-guide)

## Content

<a id="introduction"></a>

<!-- source_url: https://eventmesh.apache.org/docs/introduction/ -->

<!-- page_index: 1 -->

# Introduction to EventMesh

Version: v1.12.0

# Introduction to EventMesh

[![CI status](assets/images/ci_975a236f18bfcee2.yml)](assets/files/ci_bdaec6fb2b6bf891.yml)
[![CodeCov](assets/images/master_c8a5ef00de871e32.svg)](https://codecov.io/gh/apache/eventmesh)
[![License](assets/images/eventmesh_959ee8185ad0559f.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![GitHub Release](assets/images/eventmesh_2f2aa4e55e31b51f.svg)](https://github.com/apache/eventmesh/releases)
[![Slack Status](assets/images/slack-join-chat-blue_1405eab1c3ebd682.svg)](https://join.slack.com/t/the-asf/shared_invite/zt-1y375qcox-UW1898e4kZE_pqrNsrBM2g)

**Apache EventMesh** is a fully serverless platform used to build distributed [event-driven](https://en.wikipedia.org/wiki/Event-driven_architecture) applications.

<a id="introduction--features"></a>

## Features

Apache EventMesh has a vast amount of features to help users achieve their goals. Let us share with you some of the key features EventMesh has to offer:

- Built around the [CloudEvents](https://cloudevents.io) specification.
- Rapidly extensible language sdk around [gRPC](https://grpc.io) protocols.
- Rapidly extensible middleware by connectors such as [Apache RocketMQ](https://rocketmq.apache.org), [Apache Kafka](https://kafka.apache.org), [Apache Pulsar](https://pulsar.apache.org), [RabbitMQ](https://rabbitmq.com), [Redis](https://redis.io), [Pravega](https://cncf.pravega.io), and [RDMS](https://en.wikipedia.org/wiki/Relational_database)(in progress) using [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity).
- Rapidly extensible controller such as [Consul](https://consulproject.org/en/), [Nacos](https://nacos.io), [ETCD](https://etcd.io) and [Zookeeper](https://zookeeper.apache.org/).
- Guaranteed at-least-once delivery.
- Deliver events between multiple EventMesh deployments.
- Event schema management by catalog service.
- Powerful event orchestration by [Serverless workflow](https://serverlessworkflow.io/) engine.
- Powerful event filtering and transformation.
- Rapid, seamless scalability.
- Easy Function develop and framework integration.

- [Features](#introduction--features)

---

<a id="roadmap"></a>

<!-- source_url: https://eventmesh.apache.org/docs/roadmap/ -->

<!-- page_index: 2 -->

# Development Roadmap

Version: v1.12.0

# Development Roadmap

The development roadmap of Apache EventMesh is an overview of the planned features and milestones involved in the next several releases. The recent features and bug fixes are documented in the [Release Notes](https://eventmesh.apache.org/events/release-notes/v1.12.0/). The order of the features listed below doesn't correspond to their priorities.

<a id="roadmap--list-of-features-and-milestones"></a>

## List of Features and Milestones

<table><thead><tr><th>Status</th><th>Description</th><th>Reference</th></tr></thead><tbody><tr><td><strong>Implemented in 1.0.0</strong></td><td>Support HTTP</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.0.0</strong></td><td>Support TCP</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.0.0</strong></td><td>Support Pub/Sub Event</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.1.1</strong></td><td>Provide Java SDK</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.1.1</strong></td><td>Support HTTPS</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.2.0</strong></td><td>Support RocketMQ as EventStore</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.2.0</strong></td><td>Support Heartbeat</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.3.0</strong></td><td>Integrate with OpenSchema</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.3.0</strong></td><td>Integrate with OpenTelemetry</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.3.0</strong></td><td>Support CloudEvents</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.4.0</strong></td><td>Support gRPC</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.5.0</strong></td><td>Provide Golang SDK</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.5.0</strong></td><td>Support Nacos Registry</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.5.0</strong></td><td>Support Mesh Bridge</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.5.0</strong></td><td>Support  Federal Government</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.5.0</strong></td><td>Support Mesh Bridge</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.6.0</strong></td><td>Integrate with Consul</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.6.0</strong></td><td>Support Webhook</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.6.0</strong></td><td>Support etcd</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support Knative Eventing Infrastructure</td><td><a href="https://github.com/apache/issues/790" rel="noopener noreferrer" target="_blank">GitHub Issue</a>, <a href="https://issues.apache.org/jira/browse/COMDEV-463" rel="noopener noreferrer" target="_blank">GSoC '22</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support Pravega as EventStore</td><td><a href="https://github.com/apache/issues/270" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support Kafka as EventStore</td><td><a href="https://github.com/apache/issues/676" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support Pulsar as EventStore</td><td><a href="https://github.com/apache/issues/676" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support CNCF Serverless Workflow</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support Redis</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Provide Rust SDK</td><td><a href="https://github.com/apache/issues/815" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support Zookeeper</td><td><a href="https://github.com/apache/issues/417" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.7.0</strong></td><td>Support RabbitMQ as EventStore</td><td><a href="https://github.com/apache/issues/1553" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>Implemented in 1.8.0</strong></td><td>Provide Dashboard</td><td><a href="https://github.com/apache/issues/700" rel="noopener noreferrer" target="_blank">GitHub Issue</a>, <a href="https://issues.apache.org/jira/browse/COMDEV-465" rel="noopener noreferrer" target="_blank">GSoC '22</a></td></tr><tr><td><strong>In Progress</strong></td><td>Source/Sink Connector</td><td><a href="https://github.com/apache/eventmesh/issues/3492" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>In Progress</strong></td><td>K8s integration</td><td><a href="https://github.com/apache/eventmesh/issues/3327" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>In Progress</strong></td><td>OpenFunction integration</td><td><a href="https://github.com/apache/eventmesh/issues/2040" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td><strong>In Progress</strong></td><td>OpenSergo integration</td><td><a href="https://github.com/apache/eventmesh/issues/2805" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td>Planned</td><td>Transaction Event</td><td><a href="https://github.com/apache/issues/697" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td>Planned</td><td>Provide NodeJS SDK</td><td><a href="https://github.com/apache/eventmesh/" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td>Planned</td><td>Provide PHP    SDK</td><td><a href="https://github.com/apache/eventmesh/3" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td>Planned</td><td>Event Query Language (EQL)</td><td><a href="https://github.com/apache/eventmesh/" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr><tr><td>Planned</td><td>WebAssembly Runtime</td><td><a href="https://github.com/apache/eventmesh/" rel="noopener noreferrer" target="_blank">GitHub Issue</a></td></tr></tbody></table>
<a id="roadmap--connector-implementation-status"></a>

## Connector Implementation Status

<table><thead><tr><th align="center">Service / Middleware</th><th align="center">Source</th><th align="center">Sink</th></tr></thead><tbody><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-rocketmq" rel="noopener noreferrer" target="_blank">RocketMQ</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-kafka" rel="noopener noreferrer" target="_blank">Kafka</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-pulsar" rel="noopener noreferrer" target="_blank">Pulsar</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="#design-document-connect-rabbitmq-connector">RabbitMQ</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="#design-document-connect-http-connector">HTTP</a></td><td align="center">✅</td><td align="center">⬜</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-jdbc" rel="noopener noreferrer" target="_blank">JDBC</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-spring" rel="noopener noreferrer" target="_blank">Spring</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-openfunction" rel="noopener noreferrer" target="_blank">OpenFunction</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-file" rel="noopener noreferrer" target="_blank">File</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center">Email</td><td align="center">⬜</td><td align="center">⬜</td></tr><tr><td align="center"><a href="#design-document-connect-redis-connector">Redis</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-s3" rel="noopener noreferrer" target="_blank">S3 File</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center">ClickHouse</td><td align="center">⬜</td><td align="center">⬜</td></tr><tr><td align="center"><a href="#design-document-connect-mongodb-connector">MongoDB</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-prometheus" rel="noopener noreferrer" target="_blank">Prometheus</a></td><td align="center">✅</td><td align="center">⬜</td></tr><tr><td align="center"><a href="#design-document-connect-knative-connector">Knative</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-pravega" rel="noopener noreferrer" target="_blank">Pravega</a></td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center">More connectors will be added...</td><td align="center">N/A</td><td align="center">N/A</td></tr></tbody></table>
<table><thead><tr><th align="center">Platform / Product</th><th align="center">Source</th><th align="center">Sink</th></tr></thead><tbody><tr><td align="center"><a href="#design-document-connect-lark-connector">Feishu/Lark</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center"><a href="#design-document-connect-dingtalk-connector">DingTalk</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center"><a href="#design-document-connect-wecom-connector">WeCom</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center"><a href="https://github.com/apache/eventmesh/tree/master/eventmesh-connectors/eventmesh-connector-wechat" rel="noopener noreferrer" target="_blank">WeChat</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center">GitHub</td><td align="center">⬜</td><td align="center">⬜</td></tr><tr><td align="center">ChatGPT</td><td align="center">⬜</td><td align="center">⬜</td></tr><tr><td align="center"><a href="#design-document-connect-slack-connector">Slack</a></td><td align="center">⬜</td><td align="center">✅</td></tr><tr><td align="center">More connectors will be added...</td><td align="center">N/A</td><td align="center">N/A</td></tr></tbody></table>
<a id="roadmap--event-store-implementation-status"></a>

## Event Store Implementation Status

<table><thead><tr><th align="center">Service / Middleware</th><th align="center">Ingress</th><th align="center">Topic Management</th></tr></thead><tbody><tr><td align="center">RocketMQ</td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center">Kafka</td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center">Standalone</td><td align="center">✅</td><td align="center">✅</td></tr><tr><td align="center">Pulsar</td><td align="center">✅</td><td align="center">⬜</td></tr><tr><td align="center">RabbitMQ</td><td align="center">✅</td><td align="center">⬜</td></tr><tr><td align="center">Redis</td><td align="center">✅</td><td align="center">⬜</td></tr><tr><td align="center">Support for more Event Stores...</td><td align="center">N/A</td><td align="center">N/A</td></tr></tbody></table>

- [List of Features and Milestones](#roadmap--list-of-features-and-milestones)
- [Connector Implementation Status](#roadmap--connector-implementation-status)
- [Event Store Implementation Status](#roadmap--event-store-implementation-status)

---

<a id="instruction-store"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/store/ -->

<!-- page_index: 3 -->

# Event Store

Version: v1.12.0

# Event Store

<a id="instruction-store--1-prerequisites"></a>

## 1. Prerequisites

- 64-bit OS, we recommend Linux/Unix.
- 64-bit JDK 8 or JDK 11
- 4GB+ available disk to deploy Event Store

This document provides an example of deploying it with RocketMQ as Event Store, but you can also choose another [Event Store supported by EventMesh](#roadmap--event-store-implementation-status). If you choose default standalone mode, you could skip this file and go to the next step: Deploy EventMesh Runtime; if not, you could choose RocketMQ as the store layer.

In a production environment, you should use an Event Store other than standalone to support greater throughput and higher availability.

<a id="instruction-store--2-download"></a>

## 2. Download

Download the Binary code (recommended: 4.9.\*) from [RocketMQ Official](https://rocketmq.apache.org/download/). Here we take 4.9.4 as an example.

```shell
unzip rocketmq-all-4.9.4-bin-release.zip
cd rocketmq-4.9.4/
```

![rocketmq_1](assets/images/rocketmq-1-cf2134e63e6f1a8fd073dc6fc80d706f_639d65333c301d25.png)

<a id="instruction-store--3-start"></a>

## 3. Start

Start Name Server:

```shell
nohup sh bin/mqnamesrv &
tail -f ~/logs/rocketmqlogs/namesrv.log
```

![rocketmq_2](assets/images/rocketmq-2-6cb39241202920164fbc621facde31dd_ff08416d3f448c89.png)

Start Broker:

```shell
nohup sh bin/mqbroker -n localhost:9876 &
tail -f ~/logs/rocketmqlogs/broker.log
```

The deployment of Event Store has finished, please go to the next step: [Start EventMesh Runtime](#instruction-runtime)

<a id="instruction-store--reference"></a>

## Reference

For more details about RocketMQ, please refer to <https://rocketmq.apache.org/docs/quick-start/>.

- [1. Prerequisites](#instruction-store--1-prerequisites)
- [2. Download](#instruction-store--2-download)
- [3. Start](#instruction-store--3-start)
- [Reference](#instruction-store--reference)

---

<a id="instruction-store-with-docker"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/store-with-docker/ -->

<!-- page_index: 4 -->

# Event Store with Docker

Version: v1.12.0

# Event Store with Docker

<a id="instruction-store-with-docker--1-prerequisites"></a>

## 1. Prerequisites

- 64-bit OS, we recommend Linux/Unix.
- 4GB+ available disk to deploy Event Store

This document provides an example of deploying it with RocketMQ as Event Store, but you can also choose another [Event Store supported by EventMesh](#roadmap--event-store-implementation-status). If you choose default standalone mode, you could skip this file and go to the next step: Deploy EventMesh Runtime; if not, you could choose RocketMQ as the store layer.

In a production environment, you should use an Event Store other than standalone to support greater throughput and higher availability.

<a id="instruction-store-with-docker--2-deploy"></a>

## 2. Deploy

<a id="instruction-store-with-docker--21-pull-images"></a>

### 2.1 Pull Images

Pull RocketMQ image from Docker Hub:

```shell
#Pull rocketmq image
sudo docker pull apache/rocketmq:4.9.4
```

You can list and view existing local mirrors with the following command:

```shell
sudo docker images
```

If the terminal displays the image information as shown below, the RocketMQ image has been successfully downloaded locally.

```shell
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
apache/rocketmq   4.9.4     a2a50ca263c3   13 months ago   548MB
```

![rocketmq_docker_1](assets/images/rocketmq-docker-1-f0b1a3b2fac7c2af6a5ebbab371f79f6_c79392fa330eefb3.png)

<a id="instruction-store-with-docker--22-run-docker"></a>

### 2.2 Run Docker

Run namesrv container:

```shell
sudo docker run -d -p 9876:9876 \
  -v `pwd`/data/namesrv/logs:/root/logs \
  -v `pwd`/data/namesrv/store:/root/store \
  --name rmqnamesrv \
  apache/rocketmq:4.9.4 \
  sh mqnamesrv
```

Run broker container:

```shell
sudo docker run -d -p 10911:10911 -p 10909:10909 \
  -v `pwd`/data/broker/logs:/root/logs \
  -v `pwd`/data/broker/store:/root/store \
  --name rmqbroker \
  --link rmqnamesrv:namesrv \
  -e "NAMESRV_ADDR=namesrv:9876" \
  apache/rocketmq:4.9.4 \
  sh mqbroker -c ../conf/broker.conf
```

![rocketmq_docker_2](assets/images/rocketmq-docker-2-6bc9495c8815c12a48502db178167faa_459bc989e7297362.png)

Please note that the `rocketmq-broker ip` is `pod ip`. If you want to modify this ip, you can set it your custom value in `broker.conf`。

By now, the deployment of Event Store has finished, please go to the next step: [Start EventMesh Runtime Using Docker](#instruction-runtime-with-docker)

- [1. Prerequisites](#instruction-store-with-docker--1-prerequisites)
- [2. Deploy](#instruction-store-with-docker--2-deploy)
  - [2.1 Pull Images](#instruction-store-with-docker--21-pull-images)
  - [2.2 Run Docker](#instruction-store-with-docker--22-run-docker)

---

<a id="instruction-runtime"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/runtime/ -->

<!-- page_index: 5 -->

# EventMesh Runtime Quick Start

Version: v1.12.0

# EventMesh Runtime Quick Start

EventMesh Runtime is a stateful Mesh node in the EventMesh cluster, responsible for event transmission between Source Connectors and Sink Connectors. It uses Event Store as a storage queue for events.

![EventMesh Runtime](assets/images/runtime-a7096bf933834ceba5f954ae4786776d_6be78126ad0891dd.png)

<a id="instruction-runtime--1-binary-distribution-deployment"></a>

## 1. Binary Distribution Deployment

<a id="instruction-runtime--11-environment"></a>

### 1.1 Environment

- Recommended to use 64-bit Linux/Unix systems
- 64-bit JDK 8 or JDK 11

<a id="instruction-runtime--12-download"></a>

### 1.2 Download

Download the latest version of the Binary Distribution from the [EventMesh Download](https://eventmesh.apache.org/download) page and extract it:

```shell
wget https://dlcdn.apache.org/eventmesh/1.11.0/apache-eventmesh-1.11.0-bin.tar.gz
tar -xvzf apache-eventmesh-1.11.0-bin.tar.gz
cd apache-eventmesh-1.11.0
```

<a id="instruction-runtime--13-configuration"></a>

### 1.3 Configuration

This document provides an example of deploying it with RocketMQ as Event Store, but you can also choose another [Event Store supported by EventMesh](#roadmap--event-store-implementation-status). If you choose a non-standalone mode, ensure that [RocketMQ is successfully started](https://rocketmq.apache.org/docs/quick-start/) and accessible via IP address. If you stick to the default standalone mode, RocketMQ doesn't need to be started.

<a id="instruction-runtime--131-eventmesh-runtime-configuration"></a>

#### 1.3.1 EventMesh Runtime Configuration

This configuration file includes settings for the EventMesh Runtime environment and integrated plugins.

```shell
vim conf/eventmesh.properties
```

Specify RocketMQ as Event Store:

```properties
# storage plugin
eventMesh.storage.plugin.type=rocketmq
```

Check if the default ports in the configuration file are occupied. If occupied, modify them to unused ports:

<table><thead><tr><th>Property</th><th>Default</th><th>Remarks</th></tr></thead><tbody><tr><td>eventMesh.server.tcp.port</td><td>10000</td><td>TCP listening port</td></tr><tr><td>eventMesh.server.http.port</td><td>10105</td><td>HTTP listening port</td></tr><tr><td>eventMesh.server.grpc.port</td><td>10205</td><td>gRPC listening port</td></tr><tr><td>eventMesh.server.admin.http.port</td><td>10106</td><td>HTTP management port</td></tr></tbody></table>
<a id="instruction-runtime--132-event-store-configuration"></a>

#### 1.3.2 Event Store Configuration

In the case of RocketMQ, the configuration file includes parameters required to connect to the RocketMQ namesrv.

Edit `rocketmq-client.properties`:

```shell
vim conf/rocketmq-client.properties
```

If the namesrv address you are running is different from the default value in the configuration file, modify it to the actual running namesrv address.

<table><thead><tr><th>Property</th><th>Default</th><th>Remarks</th></tr></thead><tbody><tr><td>eventMesh.server.rocketmq.namesrvAddr</td><td>127.0.0.1:9876;127.0.0.1:9876</td><td>RocketMQ namesrv address</td></tr></tbody></table>
<a id="instruction-runtime--14-start"></a>

### 1.4 Start

Execute the `start.sh` script to start EventMesh Runtime:

```shell
bash bin/start.sh
```

If the script only prints the following three lines without any other error messages, it means the script has executed successfully:

```shell
EventMesh using Java version: 8, path: /usr/local/openjdk-8/bin/java
EVENTMESH_HOME : /data/app/eventmesh
EVENTMESH_LOG_HOME : /data/app/eventmesh/logs
```

Next, view the logs output by EventMesh to check its runtime status:

```shell
tail -n 50 -f logs/eventmesh.out
```

When the log output shows `server state:RUNNING`, it means EventMesh Runtime has started successfully.

Stop EventMesh Runtime:

```shell
bash bin/stop.sh
```

When the script prints `shutdown server ok!`, it means EventMesh Runtime has stopped.

<a id="instruction-runtime--2-build-binary-distribution"></a>

## 2. Build Binary Distribution

<a id="instruction-runtime--21-environment"></a>

### 2.1 Environment

- Recommended to use 64-bit Linux/Unix systems
- 64-bit JDK 8 or JDK 11
- [Gradle](https://docs.gradle.org/current/userguide/installation.html) 7.0+ (optional), the build commands provided in this document use the Gradle Wrapper, and you don't need to configure the Gradle environment yourself. You can also check the recommended Gradle version for your EventMesh version in the `gradle/wrapper/gradle-wrapper.properties` file and use your local Gradle version for compilation.

<a id="instruction-runtime--22-download"></a>

### 2.2 Download

Download the Source Code from [EventMesh Download](https://eventmesh.apache.org/download) and extract it:

```shell
wget https://dlcdn.apache.org/eventmesh/1.11.0/apache-eventmesh-1.11.0-source.tar.gz
tar -xvzf apache-eventmesh-1.11.0-source.tar.gz
cd apache-eventmesh-1.11.0-src/
```

You can also choose to clone the code from GitHub:

```shell
git clone https://github.com/apache/eventmesh.git
cd eventmesh/
```

<a id="instruction-runtime--23-build"></a>

### 2.3 Build

EventMesh is developed based on JDK8, and the binary distribution is also built based on JDK8. It is recommended to run EventMesh Runtime in a JDK8 environment.

<a id="instruction-runtime--run-in-a-jdk8-environment"></a>

#### Run in a JDK8 Environment

Some source code needs to be generated under JDK11:

```shell
./gradlew clean generateGrammarSource --parallel --daemon
```

The `generateGrammarSource` task will generate the source code required for `ANTLR` under the `org.apache.eventmesh.connector.jdbc.antlr4.autogeneration` package.

Next, build EventMesh Runtime under JDK8:

```shell
./gradlew clean dist -x spotlessJava -x generateGrammarSource --parallel --daemon
```

After the build is complete, proceed to [2.4 Package Plugins](#instruction-runtime--24-package-plugins).

> You can switch between JDK versions using `update-alternatives` or `JAVA_HOME` and check the current JDK version with `java -version`.

<a id="instruction-runtime--run-in-a-jdk11-environment"></a>

#### Run in a JDK11 Environment

If you want to use JDK11 as the runtime environment for EventMesh, execute:

```shell
./gradlew clean dist --parallel --daemon
```

After the build is complete, proceed to [2.4 Package Plugins](#instruction-runtime--24-package-plugins).

<a id="instruction-runtime--24-package-plugins"></a>

### 2.4 Package Plugins

The `installPlugin` task will copy the built plugins to the `dist` directory:

```shell
./gradlew installPlugin
```

EventMesh will load the plugins from the `plugin` directory based on the configuration in `eventmesh.properties`.

After a successful build, the `dist` directory in the project root contains the binary files for EventMesh. For configuration and startup, refer to [Binary Distribution Deployment](#instruction-runtime--1-binary-distribution-deployment).

<a id="instruction-runtime--3-start-from-source-code"></a>

## 3. Start from Source Code

<a id="instruction-runtime--31-dependencies"></a>

### 3.1 Dependencies

- Recommended to use 64-bit Linux/Unix systems
- 64-bit JDK 8 or JDK 11
- [Gradle](https://docs.gradle.org/current/userguide/installation.html) 7.0+ (optional), the build commands provided in this document use the Gradle Wrapper, and you don't need to configure the Gradle environment yourself. You can also check the recommended Gradle version for your EventMesh version in the `gradle/wrapper/gradle-wrapper.properties` file and use your local Gradle version for compilation.
- It is recommended to use an IDE (Integrated Development Environment) to import EventMesh. `Intellij IDEA` is recommended as the IDE.

<a id="instruction-runtime--32-download"></a>

### 3.2 Download

Clone the code from GitHub:

```shell
git clone https://github.com/apache/eventmesh.git
cd eventmesh/
```

You can also download the Source Code release from [EventMesh Download](https://eventmesh.apache.org/download) and extract it:

```shell
wget https://dlcdn.apache.org/eventmesh/1.11.0/apache-eventmesh-1.11.0-source.tar.gz
tar -xvzf apache-eventmesh-1.11.0-source.tar.gz
cd apache-eventmesh-1.11.0-src/
```

<a id="instruction-runtime--33-project-structure-explanation"></a>

### 3.3 Project Structure Explanation

<table><thead><tr><th>Main Module</th><th>Description</th></tr></thead><tbody><tr><td>eventmesh-starter</td><td>Entry point for running EventMesh locally</td></tr><tr><td>eventmesh-runtime</td><td>EventMesh Runtime, the runtime module</td></tr><tr><td>eventmesh-connectors</td><td><a href="#design-document-connect-connectors">Connectors</a> for connecting event sources and sinks, supporting <a href="#roadmap--connector-implementation-status">various services and platforms</a></td></tr><tr><td>eventmesh-storage-plugin</td><td><a href="#roadmap--event-store-implementation-status">Event Store</a> plugin for EventMesh Runtime</td></tr><tr><td>eventmesh-sdks</td><td>Multi-language client SDKs for EventMesh, including Java, Go, C and Rust</td></tr><tr><td>eventmesh-examples</td><td>Examples of SDK usage</td></tr><tr><td>eventmesh-spi</td><td>Module for loading EventMesh SPI</td></tr><tr><td>eventmesh-common</td><td>Module for common classes and methods</td></tr></tbody></table>
> Plugin modules follow the SPI specification defined by EventMesh, and custom SPI interfaces need to be annotated with `@EventMeshSPI`.
>
> Plugin instances need to be configured in the corresponding module under the `/main/resources/META-INF/eventmesh` directory with a mapping file for interface and implementation classes. The file name is the fully qualified class name of the SPI interface.
>
> The content of the file is the mapping from the plugin instance name to the plugin instance. For details, refer to the `eventmesh-storage-rocketmq` plugin module.

<a id="instruction-runtime--34-plugin-explanation"></a>

### 3.4 Plugin Explanation

<a id="instruction-runtime--341-install-plugins"></a>

#### 3.4.1 Install Plugins

EventMesh has an SPI mechanism that allows EventMesh to discover and load plugins. There are two ways to install plugins:

- Classpath loading: During local development, you can add dependencies in the `build.gradle` of the `eventmesh-starter` module. For example, to add the Kafka Storage Plugin:

```gradle
dependencies {
   implementation project(":eventmesh-runtime")
   // Example: Add the Kafka Storage Plugin
   implementation project(":eventmesh-storage-plugin:eventmesh-storage-kafka")
}
```

- File loading: By installing the plugin to the plugin directory, EventMesh will automatically load the plugins in the plugin directory based on certain conditions during runtime. Please refer to [2.3 Build](#instruction-runtime--23-build) and [2.4 Package Plugins](#instruction-runtime--24-package-plugins).

> When you make changes to the source code, it is recommended to add the `build` task to the command provided in [2.3 Build](#instruction-runtime--23-build) to recompile and run unit tests. For example:
>
>
```shell
./gradlew clean build dist -x spotlessJava -x generateGrammarSource --parallel --daemon
```

<a id="instruction-runtime--342-use-plugins"></a>

#### 3.4.2 Use Plugins

EventMesh will load the plugins by default from the `dist/plugin` directory. You can change the plugin directory using `-DeventMeshPluginDir=your_plugin_directory`. The plugin instances needed at runtime can be configured in the `confPath` directory in the `eventmesh.properties` file. For example, by setting the following, you declare the use of the RocketMQ as Event Store:

```properties
# storage plugin
eventMesh.storage.plugin.type=rocketmq
```

<a id="instruction-runtime--35-configure-vm-options"></a>

### 3.5 Configure VM Options

```properties
-Dlog4j.configurationFile=eventmesh-runtime/conf/log4j2.xml
-Deventmesh.log.home=eventmesh-runtime/logs
-Deventmesh.home=eventmesh-runtime
-DconfPath=eventmesh-runtime/conf
```

If the operating system is Windows, replace the forward slash with a backslash `\`.

<a id="instruction-runtime--36-start"></a>

### 3.6 Start

Run the `main()` method of the `org.apache.eventmesh.starter.StartUp` class in the `eventmesh-starter` module to start EventMesh Runtime.

<a id="instruction-runtime--37-stop"></a>

### 3.7 Stop

When the following logs are printed to the console, EventMesh Runtime has stopped.

```log
DEBUG StatusConsoleListener Shutdown hook enabled. Registering a new one.
WARN StatusConsoleListener Unable to register Log4j shutdown hook because JVM is shutting down. Using SimpleLogger
```

- [1. Binary Distribution Deployment](#instruction-runtime--1-binary-distribution-deployment)
  - [1.1 Environment](#instruction-runtime--11-environment)
  - [1.2 Download](#instruction-runtime--12-download)
  - [1.3 Configuration](#instruction-runtime--13-configuration)
  - [1.4 Start](#instruction-runtime--14-start)
- [2. Build Binary Distribution](#instruction-runtime--2-build-binary-distribution)
  - [2.1 Environment](#instruction-runtime--21-environment)
  - [2.2 Download](#instruction-runtime--22-download)
  - [2.3 Build](#instruction-runtime--23-build)
  - [2.4 Package Plugins](#instruction-runtime--24-package-plugins)
- [3. Start from Source Code](#instruction-runtime--3-start-from-source-code)
  - [3.1 Dependencies](#instruction-runtime--31-dependencies)
  - [3.2 Download](#instruction-runtime--32-download)
  - [3.3 Project Structure Explanation](#instruction-runtime--33-project-structure-explanation)
  - [3.4 Plugin Explanation](#instruction-runtime--34-plugin-explanation)
  - [3.5 Configure VM Options](#instruction-runtime--35-configure-vm-options)
  - [3.6 Start](#instruction-runtime--36-start)
  - [3.7 Stop](#instruction-runtime--37-stop)

---

<a id="instruction-runtime-with-docker"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/runtime-with-docker/ -->

<!-- page_index: 6 -->

# EventMesh Runtime with Docker

Version: v1.12.0

# EventMesh Runtime with Docker

You can deploy EventMesh Runtime using Docker. This document provides an example of deploying it with RocketMQ as Event Store, but you can also choose another [Event Store supported by EventMesh](#roadmap--event-store-implementation-status).

<a id="instruction-runtime-with-docker--1-prerequisites"></a>

## 1. Prerequisites

1. It is recommended to use a 64-bit Linux system.
2. Ensure Docker Engine is installed. Refer to the [official Docker documentation](https://docs.docker.com/engine/install/) for the installation process.
3. Familiarity with basic Docker concepts and command-line operations (e.g., registry, mounting) is recommended but not mandatory, as the required commands are provided.
4. If you choose a non-standalone mode, ensure that [RocketMQ is successfully started](https://rocketmq.apache.org/docs/quick-start/) and accessible via IP address. If you stick to the default standalone mode, RocketMQ doesn't need to be deployed.

<a id="instruction-runtime-with-docker--2-pull-the-eventmesh-runtime-image"></a>

## 2. Pull the EventMesh Runtime Image

First, open a command line and use the following `pull` command to download the [latest version of EventMesh](https://eventmesh.apache.org/events/release-notes/) from [Docker Hub](https://hub.docker.com/r/apache/eventmesh/tags).

```shell
sudo docker pull apache/eventmesh:latest
```

You can use the following command to list and view the locally available images.

```shell
sudo docker images
```

If the terminal displays image information similar to the following, it indicates that the EventMesh image has been successfully downloaded locally.

```shell
$ sudo docker images REPOSITORY TAG IMAGE ID CREATED SIZE apache/eventmesh latest f32f9e5e4694 2 days ago 917MB
```

<a id="instruction-runtime-with-docker--3-mount-configuration-files"></a>

## 3. Mount Configuration Files

If you are starting EventMesh Runtime in standalone mode and haven't customized the configuration, you can proceed to the next step.

First, create the EventMesh configuration file directory on the host machine. This directory can be freely specified:

```shell
sudo mkdir -p /data/eventmesh/conf
cd /data/eventmesh/conf
```

<a id="instruction-runtime-with-docker--31-eventmesh-runtime-configuration"></a>

### 3.1 EventMesh Runtime Configuration

This configuration file includes parameters required for the EventMesh Runtime environment and integration with other plugins.

Download the configuration file (replace `1.10.0` in the download link with the version you are using):

```shell
sudo wget https://raw.githubusercontent.com/apache/eventmesh/1.10.0-prepare/eventmesh-runtime/conf/eventmesh.properties
```

Edit `eventmesh.properties`:

```shell
sudo vim eventmesh.properties
```

Specify RocketMQ as Event Store:

```properties
# storage plugin
eventMesh.storage.plugin.type=rocketmq
```

Check if the default ports in the configuration file are occupied. If occupied, modify them to unused ports:

<table><thead><tr><th>Property</th><th>Default</th><th>Remarks</th></tr></thead><tbody><tr><td>eventMesh.server.tcp.port</td><td>10000</td><td>TCP listening port</td></tr><tr><td>eventMesh.server.http.port</td><td>10105</td><td>HTTP listening port</td></tr><tr><td>eventMesh.server.grpc.port</td><td>10205</td><td>gRPC listening port</td></tr><tr><td>eventMesh.server.admin.http.port</td><td>10106</td><td>HTTP management port</td></tr></tbody></table>
<a id="instruction-runtime-with-docker--32-event-store-configuration"></a>

### 3.2 Event Store Configuration

In the case of RocketMQ, the configuration file includes parameters required to connect to the RocketMQ namesrv.

Download the configuration file (replace `1.10.0` in the download link with the version you are using):

```shell
sudo wget https://raw.githubusercontent.com/apache/eventmesh/1.10.0-prepare/eventmesh-storage-plugin/eventmesh-storage-rocketmq/src/main/resources/rocketmq-client.properties
```

Edit `rocketmq-client.properties`:

```shell
sudo vim rocketmq-client.properties
```

If the namesrv address you are running is different from the default value in the configuration file, modify it to the actual running namesrv address.

<table><thead><tr><th>Property</th><th>Default</th><th>Remarks</th></tr></thead><tbody><tr><td>eventMesh.server.rocketmq.namesrvAddr</td><td>127.0.0.1:9876;127.0.0.1:9876</td><td>RocketMQ namesrv address</td></tr></tbody></table>
> If you are unable to download the configuration files using the provided links, you can find all the configuration files in the `conf` path of the EventMesh binary distribution.

<a id="instruction-runtime-with-docker--4-run-the-eventmesh-runtime-container"></a>

## 4. Run the EventMesh Runtime Container

Use the following command to start the EventMesh container:

```shell
sudo docker run -d --name eventmesh -p 10000:10000 -p 10105:10105 -p 10205:10205 -p 10106:10106 -v /data/eventmesh/conf/eventmesh.properties:/data/app/eventmesh/conf/eventmesh.properties -v /data/eventmesh/conf/rocketmq-client.properties:/data/app/eventmesh/conf/rocketmq-client.properties -t apache/eventmesh:latest
```

Explanation of `docker run` command parameters:

- `-p <host port>:<container port>`: Bind the container port to the host port. If you modified the default ports in EventMesh Runtime configuration or if the host's ports are already occupied, modify them accordingly.
- `-v <host path>:<container path>`: Mount the configuration files from the host to the container. If the path where you store EventMesh configuration files is not `/data/eventmesh/conf`, modify the host path accordingly. If you haven't customized the configuration files, please remove this parameter.
- `--name eventmesh`: Custom name for the container. This name must be unique.
- `-t apache/eventmesh:latest`: Image used by the container.

After executing the `docker run` command, the container ID will be returned. Use the following command to view the status of all running containers:

```shell
sudo docker ps
```

It will print:

```shell
CONTAINER ID   IMAGE                      COMMAND               CREATED          STATUS         PORTS                                                                                                                                                                 NAMES
b7a1546ee96a   apache/eventmesh:latest   "bash bin/start.sh"   10 seconds ago   Up 8 seconds   0.0.0.0:10000->10000/tcp, :::10000->10000/tcp, 0.0.0.0:10105-10106->10105-10106/tcp, :::10105-10106->10105-10106/tcp, 0.0.0.0:10205->10205/tcp, :::10205->10205/tcp   eventmesh
```

If the EventMesh Runtime container is not in the list printed by this command, it means the container failed to start. You can use the following command to view the logs at the time of startup (replace `eventmesh` with the container name or ID you specified):

```shell
sudo docker logs eventmesh
```

<a id="instruction-runtime-with-docker--5-view-eventmesh-logs"></a>

## 5. View EventMesh Logs

After successfully starting the EventMesh container, you can follow these steps to view the logs output by EventMesh and check the runtime status.

Enter the container (replace `eventmesh` with the container name or ID you specified):

```shell
sudo docker exec -it eventmesh /bin/bash
```

View the logs:

```shell
cd logs
tail -n 50 -f eventmesh.out
```

When the log output shows `server state:RUNNING`, it means EventMesh Runtime has started successfully.

<a id="instruction-runtime-with-docker--6-build-eventmesh-runtime-image-optional"></a>

## 6. Build EventMesh Runtime Image (Optional)

EventMesh is developed based on JDK8. The binary distribution and container image are built based on JDK8 and are also compatible with JDK11.

To run the container in a JDK8 environment, execute the following command in the root directory of the EventMesh source code:

```shell
sudo docker build -t yourname/eventmesh:yourtag -f docker/Dockerfile_jdk8 .
```

If you want to use JDK11 as the container's runtime environment, execute:

```shell
sudo docker build -t yourname/eventmesh:yourtag -f docker/Dockerfile_jdk11 .
```

- [1. Prerequisites](#instruction-runtime-with-docker--1-prerequisites)
- [2. Pull the EventMesh Runtime Image](#instruction-runtime-with-docker--2-pull-the-eventmesh-runtime-image)
- [3. Mount Configuration Files](#instruction-runtime-with-docker--3-mount-configuration-files)
  - [3.1 EventMesh Runtime Configuration](#instruction-runtime-with-docker--31-eventmesh-runtime-configuration)
  - [3.2 Event Store Configuration](#instruction-runtime-with-docker--32-event-store-configuration)
- [4. Run the EventMesh Runtime Container](#instruction-runtime-with-docker--4-run-the-eventmesh-runtime-container)
- [5. View EventMesh Logs](#instruction-runtime-with-docker--5-view-eventmesh-logs)
- [6. Build EventMesh Runtime Image (Optional)](#instruction-runtime-with-docker--6-build-eventmesh-runtime-image-optional)

---

<a id="instruction-demo"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/demo/ -->

<!-- page_index: 7 -->

# Run Java SDK Demo

Version: v1.12.0

# Run Java SDK Demo

[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.apache.eventmesh/eventmesh-sdk-java/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.apache.eventmesh/eventmesh-sdk-java)

> eventmesh-sdk-java acts as a client of EventMesh Runtime and communicates with it, to publish and subscribe the messages.
>
> The eventmesh-sdk-java supports ASYNC messages and BROADCAST messages. ASYNC messages indicate that producers only send messages and do not care about receiving reply messages. BROADCAST messages mean that producers send a message once, and all consumers subscribed to the broadcast topic will receive the message.
>
> eventmesh-sdk-java supports HTTP, TCP and gRPC protocols.

The test demos of TCP, HTTP and GRPC are in the module `eventmesh-examples`.

<a id="instruction-demo--1-tcp"></a>

## 1. TCP

<a id="instruction-demo--11-async"></a>

### 1.1 ASYNC

- Start consumer to subscribe the topic (we have created the TEST-TOPIC-TCP-ASYNC by default, you can also create other topic to test)

```text
Run the main method of org.apache.eventmesh.tcp.demo.sub.eventmeshmessage.AsyncSubscribe
```

- Start producer to publish async message

```text
Run the main method of org.apache.eventmesh.tcp.demo.pub.eventmeshmessage.AsyncPublish
```

<a id="instruction-demo--12-broadcast"></a>

### 1.2 BROADCAST

- Start subscriber to subscribe the topic (we have created the TEST-TOPIC-TCP-BROADCAST by default, you can also create other topic to test)

```text
Run the main method of org.apache.eventmesh.tcp.demo.sub.eventmeshmessage.AsyncSubscribeBroadcast
```

- Start publisher to publish async message

```text
Run the main method of org.apache.eventmesh.tcp.demo.pub.eventmeshmessage.AsyncPublishBroadcast
```

More information about EventMesh-TCP, please refer to [EventMesh TCP](#sdk-java-tcp)

<a id="instruction-demo--2-http"></a>

## 2 HTTP

> For HTTP, the eventmesh-sdk-java implements sending and subscribing to asynchronous events.
>
> In the demo, the `content` field of the Java class `EventMeshMessage` represents a special protocol. Therefore, if you are using the eventmesh-sdk-java's http-client, you only need to design the content of the protocol and provide the consumer's application at the same time.

<a id="instruction-demo--21-async"></a>

### 2.1 ASYNC

- The subscriber is a SpringBoot demo, so run this demo to start subscriber (we have created the topic TEST-TOPIC-HTTP-ASYNC by default, you can also create other topic to test)

```text
Run the main method of org.apache.eventmesh.http.demo.sub.SpringBootDemoApplication
```

- Start publisher to publish message

```text
Run the main method of org.apache.eventmesh.http.demo.pub.eventmeshmessage.AsyncPublishInstance
```

More information about EventMesh-HTTP, please refer to [EventMesh HTTP](#sdk-java-http)

<a id="instruction-demo--3-grpc"></a>

## 3 GRPC

> The eventmesh-sdk-java implements the gRPC protocol. It can asynchronously or synchronously send events to the EventMesh Runtime.
>
> It can subscribe to consume events through Webhook and event streaming, and also supports the CNCF CloudEvents protocol.

<a id="instruction-demo--31-async-publish-webhook-subscribe"></a>

### 3.1 ASYNC Publish & Webhook Subscribe

> Producers can asynchronously send events to the EventMesh Runtime without waiting for the events to be stored in the Event Store.
>
> For Webhook consumers, events will be pushed to the consumer's HTTP Endpoint URL, i.e., the consumer's `subscribeUrl`. This method is similar to the previously mentioned Http EventMesh client.

- Start publisher to publish message (we have created the topic TEST-TOPIC-GRPC-ASYNC by default, you can also create other topic to test)

```text
Run the main method of org.apache.eventmesh.grpc.pub.eventmeshmessage.AsyncPublishInstance
```

- Start webhook subscriber

```text
Run the main method of org.apache.eventmesh.grpc.sub.app.SpringBootDemoApplication
```

<a id="instruction-demo--32-sync-publish-stream-subscribe"></a>

### 3.2 SYNC Publish & Stream Subscribe

> Producers synchronously send events to the EventMesh Runtime while waiting for the events to be stored in the Event Store.
>
> For event stream consumers, events are pushed in a streaming to the `ReceiveMsgHook` client. This method is similar to the EventMesh client.

- Start Request-Reply publisher to publish message (we have created the topic TEST-TOPIC-GRPC-RR by default, you can also create other topic to test)

```text
Run the main method of org.apache.eventmesh.grpc.pub.eventmeshmessage.RequestReplyInstance
```

- Start stream subscriber

```text
Run the main method of org.apache.eventmesh.grpc.sub.EventmeshAsyncSubscribe
```

<a id="instruction-demo--33-publish-batch-message"></a>

### 3.3 Publish BATCH Message

> Asynchronously batch publish multiple events to the EventMesh Runtime.

- Start publisher to publish batch message (we have created the TEST-TOPIC-GRPC-ASYNC by default, you can also create other topic to test.)

```text
Run the main method of org.apache.eventmesh.grpc.pub.eventmeshmessage.BatchPublishInstance
```

More information about EventMesh-gRPC, please refer to [EventMesh gRPC](#sdk-java-grpc).

<a id="instruction-demo--4-run-demo-with-shell-scripts"></a>

## 4. Run Demo with shell scripts

Please refer to [Event Store](#instruction-store) and [EventMesh Runtime](#instruction-runtime) to finish the necessary deployment before try our demo.

After finishing the deployment of Store and Runtime, you can run our demos in module `eventmesh-examples`:

gradle：

```shell
cd apache-eventmesh-1.9.0-src/eventmesh-examples
gradle clean dist

cd ./dist/bin
```

![demo_1](assets/images/demo-1-b291f31a55c282cc6775f5f581787295_2261a02e5012ed63.png)

<a id="instruction-demo--41-tcp"></a>

### 4.1 TCP

<a id="instruction-demo--tcp-sub"></a>

#### TCP Sub

```shell
bash tcp_eventmeshmessage_sub.sh
```

Open the corresponding log file to view the log:

```text
cd /root/apache-eventmesh-1.9.0-src/eventmesh-examples/dist/logs
tail -f demo_tcp_pub.out
```

![demo_2](assets/images/demo-2-b61900f597947956b537e7152a515d08_8afa20ccb1370da9.png)

<a id="instruction-demo--tcp-pub"></a>

#### TCP Pub

```shell
bash tcp_pub_eventmeshmessage.sh
```

Open the corresponding log file to view the log:

```text
cd /root/apache-eventmesh-1.9.0-src/eventmesh-examples/dist/logs
tail -f demo_tcp_sub.out
```

![demo_3](assets/images/demo-3-1371c099695cba603d6fb92bc386f769_38c71056f542d9a9.png)

<a id="instruction-demo--42-tcp-broadcast"></a>

### 4.2 TCP Broadcast

<a id="instruction-demo--tcp-sub-broadcast"></a>

#### TCP Sub Broadcast

```shell
sh tcp_sub_eventmeshmessage_broadcast.sh
```

Open the corresponding log file to view the log:

```text
cd /root/apache-eventmesh-1.9.0-src/eventmesh-examples/dist/logs
tail -f demo_tcp_sub_broadcast.out
```

![demo_4](assets/images/demo-4-5031b1cb06595792ea59b7ba07da9b52_50f715d4a295cdac.png)

<a id="instruction-demo--tcp-pub-broadcast"></a>

#### TCP Pub Broadcast

```shell
sh tcp_pub_eventmeshmessage_broadcast.sh
```

Open the corresponding log file to view the log:

```text
cd /root/apache-eventmesh-1.9.0-src/eventmesh-examples/dist/logs
tail -f demo_tcp_pub_broadcast.out
```

![demo_5](assets/images/demo-5-fcc659377a2ba205aea8a61ea71807d8_2017847254bdd149.png)

<a id="instruction-demo--43-http"></a>

### 4.3 HTTP

<a id="instruction-demo--http-sub"></a>

#### HTTP Sub

```shell
sh http_sub.sh
```

Open the corresponding log file to view the log:

```text
cd /root/apache-eventmesh-1.9.0-src/eventmesh-examples/dist/logs
tail -f demo_http_sub.out
```

![demo_6](assets/images/demo-6-9bac3a1ffcbd2bb5a655c4272b95dd69_d40d1f7eee80e2b1.png)

<a id="instruction-demo--http-pub"></a>

#### HTTP Pub

```shell
sh http_pub_eventmeshmessage.sh
```

Open the corresponding log file to view the log:

```text
cd /root/apache-eventmesh-1.9.0-src/eventmesh-examples/dist/logs
tail -f demo_http_pub.out
```

![demo_7](assets/images/demo-7-b9e8974276045974d66075f3de722268_4335fe498488331c.png)

You can see the run logs for the different modes under the `/logs` directory.

- [1. TCP](#instruction-demo--1-tcp)
  - [1.1 ASYNC](#instruction-demo--11-async)
  - [1.2 BROADCAST](#instruction-demo--12-broadcast)
- [2 HTTP](#instruction-demo--2-http)
  - [2.1 ASYNC](#instruction-demo--21-async)
- [3 GRPC](#instruction-demo--3-grpc)
  - [3.1 ASYNC Publish & Webhook Subscribe](#instruction-demo--31-async-publish-webhook-subscribe)
  - [3.2 SYNC Publish & Stream Subscribe](#instruction-demo--32-sync-publish-stream-subscribe)
  - [3.3 Publish BATCH Message](#instruction-demo--33-publish-batch-message)
- [4. Run Demo with shell scripts](#instruction-demo--4-run-demo-with-shell-scripts)
  - [4.1 TCP](#instruction-demo--41-tcp)
  - [4.2 TCP Broadcast](#instruction-demo--42-tcp-broadcast)
  - [4.3 HTTP](#instruction-demo--43-http)

---

<a id="instruction-operator"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/operator/ -->

<!-- page_index: 8 -->

# Integrate EventMesh with K8S

Version: v1.12.0

# Integrate EventMesh with K8S

<a id="instruction-operator--1-dependencies"></a>

### 1. Dependencies

```text
docker
golang (version 1.19)
kubernetes (kubectl)
There is some compatibility between kubernetes an docker, please check the version compatibility between them and download the corresponding version to ensure that they work properly together.
```

<a id="instruction-operator--2-start"></a>

### 2. Start

Go to the eventmesh-operator directory.

```shell
cd eventmesh-operator
```

Install CRD into the specified k8s cluster.

```shell
make install

# Uninstall CRDs from the K8s cluster make uninstall
```

If you get error `eventmesh-operator/bin/controller-gen: No such file or directory`, Run the following command:

```shell
# download controller-gen locally if necessary. make controller-gen
# download kustomize locally if necessary. make kustomize
```

View crds information:

```shell
# run the following command to view crds information:kubectl get crds NAME CREATED AT connectors.eventmesh-operator.eventmesh 2023-11-28T01:35:21Z runtimes.eventmesh-operator.eventmesh 2023-11-28T01:35:21Z
```

Create and delete CRs:

Custom resource objects are located at: /config/samples

When deleting CR, simply replace create with delete.

```shell
# Create CR for eventmesh-runtime、eventmesh-connector-rocketmq,Creating a clusterIP lets eventmesh-runtime communicate with other components. make create

#success:
configmap/runtime-config created
runtime.eventmesh-operator.eventmesh/eventmesh-runtime created
service/runtime-cluster-service created
configmap/connector-rocketmq-config created
connectors.eventmesh-operator.eventmesh/connector-rocketmq created

# View the created Service. kubectl get service NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE runtime-cluster-service ClusterIP 10.109.209.72 <none> 10000/TCP 17s

# Delete CR make delete
```

Run eventmesh-operator create pods.

```shell
# run controller make run
# log go fmt ./... go vet ./... go run ./main.go INFO controller-runtime.metrics Metrics server is starting to listen {"addr": ":9020"} INFO setup starting manager INFO Starting server {"kind": "health probe", "addr": "[::]:8081"} INFO Starting server {"path": "/metrics", "kind": "metrics", "addr": "[::]:9020"} INFO runtime Creating a new eventMeshRuntime StatefulSet. {"StatefulSet.Namespace": "default", "StatefulSet.Name": "eventmesh-runtime-0-a"} INFO connector Creating a new Connector StatefulSet. {"StatefulSet.Namespace": "default", "StatefulSet.Name": "connector-rocketmq"} INFO runtime Successful reconciliation! INFO connector Successful reconciliation!

# After the pods are successfully started, run the following command to view pods. kubectl get pods NAME READY STATUS RESTARTS AGE connector-rocketmq-0 1/1 Running 0 12m eventmesh-runtime-0-a-0 1/1 Running 0 12m
```

- [1. Dependencies](#instruction-operator--1-dependencies)
- [2. Start](#instruction-operator--2-start)

---

<a id="instruction-faq"></a>

<!-- source_url: https://eventmesh.apache.org/docs/instruction/faq/ -->

<!-- page_index: 9 -->

# Frequently Asked Questions

Version: v1.12.0

# Frequently Asked Questions

<a id="instruction-faq--importing-into-eclipse"></a>

## Importing into Eclipse

We recommend using `Intellij IDEA` for development. If you prefer to use `Eclipse`, you can follow the steps below to import the project.

<a id="instruction-faq--prerequisites"></a>

### Prerequisites

- 64-bit JDK 1.8+
- Gradle 7.0+
- Eclipse with Gradle plugin installed

<a id="instruction-faq--download"></a>

### Download

```shell
git clone https://github.com/apache/eventmesh.git
```

<a id="instruction-faq--project-compilation-for-eclipse-environment"></a>

### Project Compilation for Eclipse Environment

Open the command-line terminal and run `./gradlew cleanEclipse eclipse`.

<a id="instruction-faq--configuration-modifications"></a>

### Configuration Modifications

Modify the project name to match the parameters in the `settings.gradle` configuration file, specifically the `rootProject.name` parameter.

<a id="instruction-faq--modify-the-eclipseinit-configuration-file"></a>

### Modify the `eclipse.init` Configuration File

Configure Lombok, using version 1.18.8 as an example:

```text
-javaagent:lombok-1.18.8.jar
-XBootclasspath/a:lombok-1.18.8.jar
```

<a id="instruction-faq--eclipse-configuration-for-version-202106"></a>

### Eclipse Configuration for Version 202106

Add the configuration parameter to `eclipse.init`: `--illegal-access=permit`

<a id="instruction-faq--import"></a>

### Import

Open Eclipse and import the EventMesh project into the IDE.

- [Importing into Eclipse](#instruction-faq--importing-into-eclipse)
  - [Prerequisites](#instruction-faq--prerequisites)
  - [Download](#instruction-faq--download)
  - [Project Compilation for Eclipse Environment](#instruction-faq--project-compilation-for-eclipse-environment)
  - [Configuration Modifications](#instruction-faq--configuration-modifications)
  - [Modify the `eclipse.init` Configuration File](#instruction-faq--modify-the-eclipseinit-configuration-file)
  - [Eclipse Configuration for Version 202106](#instruction-faq--eclipse-configuration-for-version-202106)
  - [Import](#instruction-faq--import)

---

<a id="design-document-event-handling-and-integration-runtime-protocol"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/event-handling-and-integration/runtime-protocol/ -->

<!-- page_index: 10 -->

# EventMesh Runtime Protocol

Version: v1.12.0

# EventMesh Runtime Protocol

<a id="design-document-event-handling-and-integration-runtime-protocol--tcp-protocol"></a>

## TCP Protocol

<a id="design-document-event-handling-and-integration-runtime-protocol--protocol-format"></a>

### Protocol Format

<table><thead><tr><th>Name</th><th>Size</th><th>Description</th></tr></thead><tbody><tr><td>Magic Code</td><td>9 bytes</td><td>Default: <code>EventMesh</code></td></tr><tr><td>Protocol Version</td><td>4 bytes</td><td>Default: <code>0000</code></td></tr><tr><td>Message Size</td><td>4 bytes</td><td>The total length of the message</td></tr><tr><td>Header Size</td><td>4 bytes</td><td>The length of the message header</td></tr><tr><td>Message Body</td><td></td><td>The content of the message</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--message-object-in-the-business-logic-layer"></a>

### Message Object in the Business Logic Layer

<a id="design-document-event-handling-and-integration-runtime-protocol--message-composition"></a>

#### Message Composition

The `Package` class in the [`Package.java` file](https://github.com/apache/eventmesh/blob/master/eventmesh-common/src/main/java/org/apache/eventmesh/common/protocol/tcp/Package.java) is the TCP message object used in business logic layer. The class contains the `header` and `body` fields.

```java
public class Package {
   private Header header;
   private Object body;
}

public class Header {
   private Command cmd;
   private int code;
   private String msg;
   private String seq;
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--specification"></a>

#### Specification

- Message Header (the `header` field): The `cmd` field in the `Header` class specifies the different types of messages.
- Message Body (the `body` field): The type of the message body should be defined based on `cmd` field in the `Header` class.

<table><thead><tr><th>Command</th><th>Type of Body</th></tr></thead><tbody><tr><td>HEARTBEAT_REQUEST, HEARTBEAT_RESPONSE, HELLO_RESPONSE, CLIENT_GOODBYE_REQUEST, CLIENT_GOODBYE_RESPONSE, SERVER_GOODBYE_REQUEST, SERVER_GOODBYE_RESPONSE, LISTEN_REQUEST, LISTEN_RESPONSE, UNSUBSCRIBE_REQUEST, SUBSCRIBE_RESPONSE, UNSUBSCRIBE_RESPONSE, ASYNC_MESSAGE_TO_SERVER_ACK, BROADCAST_MESSAGE_TO_SERVER_ACK</td><td>N/A</td></tr><tr><td>HELLO_REQUEST</td><td>UserAgent</td></tr><tr><td>SUBSCRIBE_REQUEST</td><td>Subscription</td></tr><tr><td>REQUEST_TO_SERVER, REQUEST_TO_CLIENT, RESPONSE_TO_SERVER, RESPONSE_TO_CLIENT, ASYNC_MESSAGE_TO_SERVER, ASYNC_MESSAGE_TO_CLIENT, BROADCAST_MESSAGE_TO_SERVER, BROADCAST_MESSAGE_TO_CLIENT, ASYNC_MESSAGE_TO_CLIENT_ACK, BROADCAST_MESSAGE_TO_CLIENT_ACK, RESPONSE_TO_CLIENT_ACK, REQUEST_TO_CLIENT_ACK</td><td>OpenMessage</td></tr><tr><td>REDIRECT_TO_CLIENT</td><td>RedirectInfo</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--example-of-client-server-interaction"></a>

### Example of Client-Server Interaction

```java
public enum Command {
    // Heartbeat
    HEARTBEAT_REQUEST(0),                              // Client send heartbeat request to server
    HEARTBEAT_RESPONSE(1),                             // Server reply heartbeat response to client

    // Hello
    HELLO_REQUEST(2),                                  // Client send connect request to server
    HELLO_RESPONSE(3),                                 // Server reply connect response to client

    // Disconncet
    CLIENT_GOODBYE_REQUEST(4),                         // Client send disconnect request to server
    CLIENT_GOODBYE_RESPONSE(5),                        // Server reply disconnect response to client
    SERVER_GOODBYE_REQUEST(6),                         // Server send disconncet request to client
    SERVER_GOODBYE_RESPONSE(7),                        // Client reply disconnect response to server

    // Subscribe and UnSubscribe
    SUBSCRIBE_REQUEST(8),                              // Slient send subscribe request to server
    SUBSCRIBE_RESPONSE(9),                             // Server reply subscribe response to client
    UNSUBSCRIBE_REQUEST(10),                           // Client send unsubscribe request to server
    UNSUBSCRIBE_RESPONSE(11),                          // Server reply unsubscribe response to client

    // Listen
    LISTEN_REQUEST(12),                                // Client send listen request to server
    LISTEN_RESPONSE(13),                               // Server reply listen response to client

    // Send sync message
    REQUEST_TO_SERVER(14),                             // Client (Producer) send sync message to server
    REQUEST_TO_CLIENT(15),                             // Server push sync message to client(Consumer)
    REQUEST_TO_CLIENT_ACK(16),                         // Client (Consumer) send ack of sync message to server
    RESPONSE_TO_SERVER(17),                            // Client (Consumer) send reply message to server
    RESPONSE_TO_CLIENT(18),                            // Server push reply message to client(Producer)
    RESPONSE_TO_CLIENT_ACK(19),                        // Client (Producer) send acknowledgement of reply message to server

    // Send async message
    ASYNC_MESSAGE_TO_SERVER(20),                       // Client send async msg to server
    ASYNC_MESSAGE_TO_SERVER_ACK(21),                   // Server reply ack of async msg to client
    ASYNC_MESSAGE_TO_CLIENT(22),                       // Server push async msg to client
    ASYNC_MESSAGE_TO_CLIENT_ACK(23),                   // Client reply ack of async msg to server

    // Send broadcast message
    BROADCAST_MESSAGE_TO_SERVER(24),                   // Client send broadcast msg to server
    BROADCAST_MESSAGE_TO_SERVER_ACK(25),               // Server reply ack of broadcast msg to client
    BROADCAST_MESSAGE_TO_CLIENT(26),                   // Server push broadcast msg to client
    BROADCAST_MESSAGE_TO_CLIENT_ACK(27),               // Client reply ack of broadcast msg to server

    // Redirect
    REDIRECT_TO_CLIENT(30),                            // Server send redirect instruction to client
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--client-initiated-interaction"></a>

### Client-Initiated Interaction

<table><thead><tr><th>Scene</th><th>Client Request</th><th>Server Response</th></tr></thead><tbody><tr><td>Hello</td><td>HELLO_REQUEST</td><td>HELLO_RESPONSE</td></tr><tr><td>Heartbeat</td><td>HEARTBEAT_REQUEST</td><td>HEARTBEAT_RESPONSE</td></tr><tr><td>Subscribe</td><td>SUBSCRIBE_REQUEST</td><td>SUBSCRIBE_RESPONSE</td></tr><tr><td>Unsubscribe</td><td>UNSUBSCRIBE_REQUEST</td><td>UNSUBSCRIBE_RESPONSE</td></tr><tr><td>Listen</td><td>LISTEN_REQUEST</td><td>LISTEN_RESPONSE</td></tr><tr><td>Send sync message</td><td>REQUEST_TO_SERVER</td><td>RESPONSE_TO_CLIENT</td></tr><tr><td>Send the response of sync message</td><td>RESPONSE_TO_SERVER</td><td>N/A</td></tr><tr><td>Send async message</td><td>ASYNC_MESSAGE_TO_SERVER</td><td>ASYNC_MESSAGE_TO_SERVER_ACK</td></tr><tr><td>Send broadcast message</td><td>BROADCAST_MESSAGE_TO_SERVER</td><td>BROADCAST_MESSAGE_TO_SERVER_ACK</td></tr><tr><td>Client start to disconnect</td><td>CLIENT_GOODBYE_REQUEST</td><td>CLIENT_GOODBYE_RESPONSE</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--server-initiated-interaction"></a>

### Server-Initiated Interaction

<table><thead><tr><th>Scene</th><th>Server Request</th><th>Client Response</th><th>Remark</th></tr></thead><tbody><tr><td>Push sync message to client</td><td>REQUEST_TO_CLIENT</td><td>REQUEST_TO_CLIENT_ACK</td><td></td></tr><tr><td>Push the response message of sync message to client</td><td>RESPONSE_TO_CLIENT</td><td>RESPONSE_TO_CLIENT_ACK</td><td></td></tr><tr><td>Push async message to client</td><td>ASYNC_MESSAGE_TO_CLIENT</td><td>ASYNC_MESSAGE_TO_CLIENT_ACK</td><td></td></tr><tr><td>Push broadcast message to client</td><td>BROADCAST_MESSAGE_TO_CLIENT</td><td>BROADCAST_MESSAGE_TO_CLIENT_ACK</td><td></td></tr><tr><td>Server start to disconnect</td><td>SERVER_GOODBYE_REQUEST</td><td>--</td><td></td></tr><tr><td>Server send redirect</td><td>REDIRECT_TO_CLIENT</td><td>--</td><td></td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--type-of-message"></a>

### Type of Message

<a id="design-document-event-handling-and-integration-runtime-protocol--sync-message"></a>

#### Sync Message

![Sync Message](assets/images/sync-message-6ef285bf8186ea210cdf95f6f6cfa593_c33a0923ddea893f.png)

<a id="design-document-event-handling-and-integration-runtime-protocol--async-message"></a>

#### Async Message

![Async Message](assets/images/async-message-628b4635b65593b1f2e6d8fbd7c0a38f_22a5c178290779b7.png)

<a id="design-document-event-handling-and-integration-runtime-protocol--boardcast-message"></a>

#### Boardcast Message

![Boardcast Message](assets/images/broadcast-message-d3d27b42c2c0c80a39362fb706e184f8_39a90d78c0c72632.png)

<a id="design-document-event-handling-and-integration-runtime-protocol--http-protocol"></a>

## HTTP Protocol

<a id="design-document-event-handling-and-integration-runtime-protocol--protocol-format-1"></a>

### Protocol Format

The `EventMeshMessage` class in the [`EventMeshMessage.java` file](https://github.com/apache/eventmesh/blob/master/eventmesh-common/src/main/java/org/apache/eventmesh/common/EventMeshMessage.java) is the HTTP message definition of EventMesh Runtime.

```java
public class EventMeshMessage {
    private String bizSeqNo;

    private String uniqueId;

    private String topic;

    private String content;

    private Map<String, String> prop;

    private final long createTime = System.currentTimeMillis();
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--http-post-request"></a>

### HTTP Post Request

<a id="design-document-event-handling-and-integration-runtime-protocol--heartbeat-message"></a>

#### Heartbeat Message

<a id="design-document-event-handling-and-integration-runtime-protocol--request-header"></a>

##### Request Header

<table><thead><tr><th>Key</th><th>Description</th></tr></thead><tbody><tr><td>Env</td><td>Enviroment of Client</td></tr><tr><td>Region</td><td>Region of Client</td></tr><tr><td>Idc</td><td>IDC of Client</td></tr><tr><td>Dcn</td><td>DCN of Client</td></tr><tr><td>Sys</td><td>Subsystem ID of Client</td></tr><tr><td>Pid</td><td>Client Process ID</td></tr><tr><td>Ip</td><td>Client Ip</td></tr><tr><td>Username</td><td>Client username</td></tr><tr><td>Passwd</td><td>Client password</td></tr><tr><td>Version</td><td>Protocol version</td></tr><tr><td>Language</td><td>Develop language</td></tr><tr><td>Code</td><td>Request Code</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--request-body"></a>

##### Request Body

<table><thead><tr><th>Key</th><th>Description</th></tr></thead><tbody><tr><td><code>clientType</code></td><td><code>ClientType.PUB</code> for Producer, <code>ClientType.SUB</code> for Consumer</td></tr><tr><td><code>heartbeatEntities</code></td><td>Topic, URL, etc.</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--subscribe-message"></a>

#### Subscribe Message

<a id="design-document-event-handling-and-integration-runtime-protocol--request-header-1"></a>

##### Request Header

The request header of the Subscribe message is identical to the request header of the Heartbeat message.

<a id="design-document-event-handling-and-integration-runtime-protocol--request-body-1"></a>

##### Request Body

<table><thead><tr><th>Key</th><th>Description</th></tr></thead><tbody><tr><td><code>topic</code></td><td>The topic that the client requested to subscribe to</td></tr><tr><td><code>url</code></td><td>The callback URL of the client</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--unsubscribe-message"></a>

#### Unsubscribe Message

<a id="design-document-event-handling-and-integration-runtime-protocol--request-header-2"></a>

##### Request Header

The request header of the Unsubscribe message is identical to the request header of the Heartbeat message.

<a id="design-document-event-handling-and-integration-runtime-protocol--request-body-2"></a>

##### Request Body

The request body of the Unsubscribe message is identical to the request body of the Subscribe message.

<a id="design-document-event-handling-and-integration-runtime-protocol--send-async-message"></a>

#### Send Async Message

<a id="design-document-event-handling-and-integration-runtime-protocol--request-header-3"></a>

##### Request Header

The request header of the Send Async message is identical to the request header of the Heartbeat message.

<a id="design-document-event-handling-and-integration-runtime-protocol--request-body-3"></a>

##### Request Body

<table><thead><tr><th>Key</th><th>Description</th></tr></thead><tbody><tr><td><code>topic</code></td><td>Topic of the message</td></tr><tr><td><code>content</code></td><td>The content of the message</td></tr><tr><td><code>ttl</code></td><td>The time-to-live of the message</td></tr><tr><td><code>bizSeqNo</code></td><td>The biz sequence number of the message</td></tr><tr><td><code>uniqueId</code></td><td>The unique ID of the message</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--client-initiated-interaction-1"></a>

### Client-Initiated Interaction

<table><thead><tr><th>Scene</th><th>Client Request</th><th>Server Response</th><th>Remark</th></tr></thead><tbody><tr><td>Heartbeat</td><td>HEARTBEAT(203)</td><td>SUCCESS(0) or EVENTMESH_HEARTBEAT_ERROR(19)</td><td></td></tr><tr><td>Subscribe</td><td>SUBSCRIBE(206)</td><td>SUCCESS(0) or EVENTMESH_SUBSCRIBE_ERROR(17)</td><td></td></tr><tr><td>Unsubscribe</td><td>UNSUBSCRIBE(207)</td><td>SUCCESS(0) or EVENTMESH_UNSUBSCRIBE_ERROR(18)</td><td></td></tr><tr><td>Send async message</td><td>MSG_SEND_ASYNC(104)</td><td>SUCCESS(0) or EVENTMESH_SEND_ASYNC_MSG_ERR(14)</td><td></td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--server-initiated-interaction-1"></a>

### Server-Initiated Interaction

<table><thead><tr><th>Scene</th><th>Client Request</th><th>Server Response</th><th>Remark</th></tr></thead><tbody><tr><td>Push async message to the client</td><td>HTTP_PUSH_CLIENT_ASYNC(105)</td><td><code>retCode</code></td><td>The push is successful if the <code>retCode</code> is <code>0</code></td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-runtime-protocol--grpc-protocol"></a>

## gRPC Protocol

<a id="design-document-event-handling-and-integration-runtime-protocol--protobuf"></a>

### Protobuf

The `eventmesh-protocol-gprc` module contains the [protobuf definition file](https://github.com/apache/eventmesh/blob/master/eventmesh-protocol-plugin/eventmesh-protocol-grpc/src/main/proto/eventmesh-client.proto) of the EventMesh client. The `gradle build` command generates the gRPC codes, which are located in `/build/generated/source/proto/main`. The generated gRPC codes are used in `eventmesh-sdk-java` module.

<a id="design-document-event-handling-and-integration-runtime-protocol--data-model"></a>

### Data Model

<a id="design-document-event-handling-and-integration-runtime-protocol--message"></a>

#### Message

The message data model used by `publish()`, `requestReply()` and `broadcast()` APIs is defined as:

```protobuf
message RequestHeader {
    string env = 1;
    string region = 2;
    string idc = 3;
    string ip = 4;
    string pid = 5;
    string sys = 6;
    string username = 7;
    string password = 8;
    string language = 9;
    string protocolType = 10;
    string protocolVersion = 11;
    string protocolDesc = 12;
}

message SimpleMessage {
   RequestHeader header = 1;
   string producerGroup = 2;
   string topic = 3;
   string content = 4;
   string ttl = 5;
   string uniqueId = 6;
   string seqNum = 7;
   string tag = 8;
   map<string, string> properties = 9;
}

message BatchMessage {
   RequestHeader header = 1;
   string producerGroup = 2;
   string topic = 3;

   message MessageItem {
      string content = 1;
      string ttl = 2;
      string uniqueId = 3;
      string seqNum = 4;
      string tag = 5;
      map<string, string> properties = 6;
   }

   repeated MessageItem messageItem = 4;
}

message Response {
   string respCode = 1;
   string respMsg = 2;
   string respTime = 3;
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--subscription"></a>

#### Subscription

The subscription data model used by `subscribe()` and `unsubscribe()` APIs is defined as:

```protobuf
message Subscription {
   RequestHeader header = 1;
   string consumerGroup = 2;

   message SubscriptionItem {
      enum SubscriptionMode {
         CLUSTERING = 0;
         BROADCASTING = 1;
      }

      enum SubscriptionType {
         ASYNC = 0;
         SYNC = 1;
      }

      string topic = 1;
      SubscriptionMode mode = 2;
      SubscriptionType type = 3;
   }

   repeated SubscriptionItem subscriptionItems = 3;
   string url = 4;
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--heartbeat"></a>

#### Heartbeat

The heartbeat data model used by the `heartbeat()` API is defined as:

```protobuf
message Heartbeat {
  enum ClientType {
     PUB = 0;
     SUB = 1;
  }

  RequestHeader header = 1;
  ClientType clientType = 2;
  string producerGroup = 3;
  string consumerGroup = 4;

  message HeartbeatItem {
     string topic = 1;
     string url = 2;
  }

  repeated HeartbeatItem heartbeatItems = 5;
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--service-definition"></a>

### Service Definition

<a id="design-document-event-handling-and-integration-runtime-protocol--event-publisher-service"></a>

#### Event Publisher Service

```protobuf
service PublisherService {
   // Async event publish
   rpc publish(SimpleMessage) returns (Response);

   // Sync event publish
   rpc requestReply(SimpleMessage) returns (Response);

   // Batch event publish
   rpc batchPublish(BatchMessage) returns (Response);
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--event-consumer-service"></a>

#### Event Consumer Service

```protobuf
service ConsumerService {
   // The subscribed event will be delivered by invoking the webhook url in the Subscription
   rpc subscribe(Subscription) returns (Response);

   // The subscribed event will be delivered through stream of Message
   rpc subscribeStream(Subscription) returns (stream SimpleMessage);

   rpc unsubscribe(Subscription) returns (Response);
}
```

<a id="design-document-event-handling-and-integration-runtime-protocol--client-hearthbeat-service"></a>

#### Client Hearthbeat Service

```protobuf
service HeartbeatService {
   rpc heartbeat(Heartbeat) returns (Response);
}
```

- [TCP Protocol](#design-document-event-handling-and-integration-runtime-protocol--tcp-protocol)
  - [Protocol Format](#design-document-event-handling-and-integration-runtime-protocol--protocol-format)
  - [Message Object in the Business Logic Layer](#design-document-event-handling-and-integration-runtime-protocol--message-object-in-the-business-logic-layer)
  - [Example of Client-Server Interaction](#design-document-event-handling-and-integration-runtime-protocol--example-of-client-server-interaction)
  - [Client-Initiated Interaction](#design-document-event-handling-and-integration-runtime-protocol--client-initiated-interaction)
  - [Server-Initiated Interaction](#design-document-event-handling-and-integration-runtime-protocol--server-initiated-interaction)
  - [Type of Message](#design-document-event-handling-and-integration-runtime-protocol--type-of-message)
- [HTTP Protocol](#design-document-event-handling-and-integration-runtime-protocol--http-protocol)
  - [Protocol Format](#design-document-event-handling-and-integration-runtime-protocol--protocol-format-1)
  - [HTTP Post Request](#design-document-event-handling-and-integration-runtime-protocol--http-post-request)
  - [Client-Initiated Interaction](#design-document-event-handling-and-integration-runtime-protocol--client-initiated-interaction-1)
  - [Server-Initiated Interaction](#design-document-event-handling-and-integration-runtime-protocol--server-initiated-interaction-1)
- [gRPC Protocol](#design-document-event-handling-and-integration-runtime-protocol--grpc-protocol)
  - [Protobuf](#design-document-event-handling-and-integration-runtime-protocol--protobuf)
  - [Data Model](#design-document-event-handling-and-integration-runtime-protocol--data-model)
  - [Service Definition](#design-document-event-handling-and-integration-runtime-protocol--service-definition)

---

<a id="design-document-event-handling-and-integration-https"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/event-handling-and-integration/https/ -->

<!-- page_index: 11 -->

# HTTPS

Version: v1.12.0

# HTTPS

1. Configuration in eventmesh-runtime

```text
eventMesh.properties (add the following configurations)
eventMesh.server.useTls.enabled=true   // Default value: false

Configuring environment variable
-Dssl.server.protocol=TLSv1.1   // Default value: TLSv1.1
-Dssl.server.cer=sChat2.jks     // Place the file in the conPath directory specified by the startup script start.sh
-Dssl.server.pass=sNetty
```

2. Configuration in eventmesh-sdk-java

```text
// Create a producer
LiteClientConfig eventMeshHttpClientConfig = new LiteClientConfig();
...

// Enable TLS
eventMeshHttpClientConfig.setUseTls(true);
LiteProducer producer = new LiteProducer(eventMeshHttpClientConfig);

// Configure environment variables
-Dssl.client.protocol=TLSv1.1   // Default value: TLSv1.1
-Dssl.client.cer=sChat2.jks     // Place the file in the conPath directory specified by the application
-Dssl.client.pass=sNetty
```

---

<a id="design-document-event-handling-and-integration-cloudevents"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/event-handling-and-integration/cloudevents/ -->

<!-- page_index: 12 -->

# CloudEvents Integration

Version: v1.12.0

# CloudEvents Integration

<a id="design-document-event-handling-and-integration-cloudevents--introduction"></a>

## Introduction

[CloudEvents](https://github.com/cloudevents/spec) is a specification for describing event data in common formats to provide interoperability across services, platforms and systems.

As of May 2021, EventMesh contains the following major components: `eventmesh-runtime`, `eventmesh-sdk-java` and `eventmesh-connector-rocketmq`.
For a customer to use EventMesh, `eventmesh-runtime` can be deployed as microservices to transmit
customer's events between event producers and consumers. Customer's applications can then interact
with `eventmesh-runtime` using `eventmesh-sdk-java` to publish/subscribe for events on given topics.

CloudEvents support has been a highly desired feature by EventMesh users. There are many reasons
for users to prefer using a SDK with CloudEvents support:

- CloudEvents is a more widely accepted and supported way to describe events. `eventmesh-sdk-java`
  currently uses the `EventMeshMessage` structure to describe events, which is less standardized.
- CloudEvents's Java SDK has a wider range of distribution methods. For example, EventMesh users
  currently need to use the SDK tarball or build from source for every EventMesh release. With
  CloudEvents support, it's easier for users to take a dependency on EventMesh's SDK using CloudEvents's public distributions (e.g. through a Maven configuration).
- CloudEvents's SDK supports multiple languages. Although EventMesh currently only supports a Java SDK, in future if more languages need to be supported, the extensions can be easier with experience on binding Java SDK with CloudEvents.

<a id="design-document-event-handling-and-integration-cloudevents--requirements"></a>

## Requirements

<a id="design-document-event-handling-and-integration-cloudevents--functional-requirements"></a>

### Functional Requirements

<table><thead><tr><th>Requirement ID</th><th>Requirement Description</th><th>Comments</th></tr></thead><tbody><tr><td>F-1</td><td>EventMesh users should be able to depend on a public SDK to publish/subscribe events in CloudEvents format</td><td>Functionality</td></tr><tr><td>F-2</td><td>EventMesh users should continue to have access to existing EventMesh client features (e.g. load balancing) with an SDK that supports CloudEvent</td><td>Feature Parity</td></tr><tr><td>F-3</td><td>EventMesh developers should be able to sync <code>eventmesh-sdk-java</code> and an SDK with CloudEvents support without much effort/pain</td><td>Maintainability</td></tr><tr><td>F-4</td><td>EventMesh support pluggable protocols for developers integrate other protocols (e.g. CloudEvents\EventMesh Message\OpenMessage\MQTT ...)</td><td>Functionality</td></tr><tr><td>F-5</td><td>EventMesh support the unified api for publish/subscribe events to/from Event Store</td><td>Functionality</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-cloudevents--performance-requirements"></a>

### Performance Requirements

<table><thead><tr><th>Requirement ID</th><th>Requirement Description</th><th>Comments</th></tr></thead><tbody><tr><td>P-1</td><td>Client side latency for SDK with CloudEvents support should be similar to current SDK</td><td></td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-cloudevents--design-details"></a>

## Design Details

Binding with the CloudEvents Java SDK (similar to what Kafka already did, see Reference for more details)
should be an easy way to achieve the requirements.

<a id="design-document-event-handling-and-integration-cloudevents--pluggable-protocols"></a>

### Pluggable Protocols

![Pluggable Protocols](assets/images/cloudevents-pluggable-protocols-006804094b52dd966d0f4c7f1de36f81_1f954e63e7555d61.png)

<a id="design-document-event-handling-and-integration-cloudevents--process-of-cloudevents-under-eventmesh"></a>

### Process of CloudEvents under EventMesh

<a id="design-document-event-handling-and-integration-cloudevents--for-tcp"></a>

#### For TCP

<a id="design-document-event-handling-and-integration-cloudevents--sdk-side-for-publish"></a>

##### SDK side for publish

- add the CloudEvents identifier in `package` header
- use `CloudEventBuilder` build the CloudEvent and put it into the `package` body

<a id="design-document-event-handling-and-integration-cloudevents--sdk-side-for-subscribe"></a>

##### SDK side for subscribe

- add `convert` function under the `ReceiveMsgHook` interface, for converting the `package` body to the specific protocol with the identifier in `package` header
- different protocols should implement the `ReceiveMsgHook` interface

<a id="design-document-event-handling-and-integration-cloudevents--server-side-for-publish"></a>

##### Server side for publish

- design the protocol convert api contains `decodeMessage` interface which convert the package's body to CloudEvent
- update `Session.upstreamMsg()` in `MessageTransferTask` change the input parameter Message to CloudEvent, the CloudEvent use the last step `decodeMessage` api convert
- update `SessionSender.send()` change the input parameter `Message` to `CloudEvent`
- update `MeshMQProducer` api support send `CloudEvents` in runtime
- support the implementation in `connector-plugin` for send `CloudEvents` to EventStore

<a id="design-document-event-handling-and-integration-cloudevents--server-side-for-subscribe"></a>

##### Server side for subscribe

- support change the `RocketMessage` to `CloudEvent` in connector-plugin
- overwrite the `AsyncMessageListener.consume()` function, change the input parameter `Message` to `CloudEvent`
- update the `MeshMQPushConsumer.updateOffset()` implementation change the the input parameter `Message` to `CloudEvent`
- update `DownStreamMsgContext` , change the input parameter `Message` to `CloudEvent`, update the `DownStreamMsgContext.ackMsg`

<a id="design-document-event-handling-and-integration-cloudevents--for-http"></a>

#### For HTTP

<a id="design-document-event-handling-and-integration-cloudevents--sdk-side-for-publish-1"></a>

##### SDK side for publish

- support `LiteProducer.publish(cloudEvent)`
- add the CloudEvents identifier in http request header

<a id="design-document-event-handling-and-integration-cloudevents--sdk-side-for-subscribe-1"></a>

##### SDK side for subscribe

<a id="design-document-event-handling-and-integration-cloudevents--server-side-for-publish-1"></a>

##### Server side for publish

- support build the `HttpCommand.body` by pluggable protocol plugins according the protocol type in `HttpCommand` header
- support publish the CloudEvent in message processors

<a id="design-document-event-handling-and-integration-cloudevents--server-side-for-subscribe-1"></a>

##### Server side for subscribe

- update the `EventMeshConsumer.subscribe()`
- update `HandleMsgContext` , change the input parameter `Message` to `CloudEvent`
- update `AsyncHttpPushRequest.tryHTTPRequest()`

<a id="design-document-event-handling-and-integration-cloudevents--appendix"></a>

## Appendix

<a id="design-document-event-handling-and-integration-cloudevents--references"></a>

### References

- <https://cloudevents.github.io/sdk-java/kafka>

- [Introduction](#design-document-event-handling-and-integration-cloudevents--introduction)
- [Requirements](#design-document-event-handling-and-integration-cloudevents--requirements)
  - [Functional Requirements](#design-document-event-handling-and-integration-cloudevents--functional-requirements)
  - [Performance Requirements](#design-document-event-handling-and-integration-cloudevents--performance-requirements)
- [Design Details](#design-document-event-handling-and-integration-cloudevents--design-details)
  - [Pluggable Protocols](#design-document-event-handling-and-integration-cloudevents--pluggable-protocols)
  - [Process of CloudEvents under EventMesh](#design-document-event-handling-and-integration-cloudevents--process-of-cloudevents-under-eventmesh)
- [Appendix](#design-document-event-handling-and-integration-cloudevents--appendix)
  - [References](#design-document-event-handling-and-integration-cloudevents--references)

---

<a id="design-document-event-handling-and-integration-event-bridge"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/event-handling-and-integration/event-bridge/ -->

<!-- page_index: 13 -->

# Event Bridge

Version: v1.12.0

# Event Bridge

![event-bridge](assets/images/eventmesh-bridge-94fe48311de2a164b839f5a127dccca5_30709a0c2b33f939.png)

Event Bridge supports message delivery across mesh clusters. Below is a detailed design and experience steps for this feature.

![event-bridge-detail](assets/images/event-bridge-detail-5594664b853c1294bba396d00fdaa80d_5bb08278de5aae3e.png)

> Note: To experience this feature locally, you need to start two EventMesh instances and modify the port configuration in the `eventmesh-runtime` directory's `eventmesh.properties` file to avoid port conflicts. For the sake of the following descriptions, the event-bridge feature is presented according to the information in the above diagram.

<a id="design-document-event-handling-and-integration-event-bridge--01-remote-subscription"></a>

## 01 Remote Subscription

**Description**: Initiates a remote subscription command to cluster2 EventMesh. Upon receiving the command, cluster2 EventMesh will invoke the local subscription interface of cluster1 EventMesh with the subscription information.

**URL**: http://{cluster2 address}/eventmesh/subscribe/remote

**Request Method**: POST

**Request Parameters**: application/json format

<table><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>String</td><td>Yes</td><td>Identifies the subscription URL, temporarily useless, will be replaced by (/eventmesh/bridge/publish) later, currently only for strong validation, will actually be replaced by the cluster2 EventMesh configuration information</td></tr><tr><td>consumerGroup</td><td>String</td><td>Yes</td><td>Identifies the consumer group information, will be replaced by the configuration information of cluster2 EventMesh</td></tr><tr><td>topic</td><td>List</td><td>Yes</td><td>Identifies the subscription information list</td></tr><tr><td>mode</td><td>String</td><td>Yes</td><td>Identifies the consumption mode, divided into clustering mode and broadcast mode</td></tr><tr><td>topic</td><td>String</td><td>Yes</td><td>Identifies the subscribed topic</td></tr><tr><td>type</td><td>String</td><td>Yes</td><td>Identifies the consumption type, divided into synchronous and asynchronous</td></tr><tr><td>remoteMesh</td><td>String</td><td>No</td><td>Identifies the remote mesh address, prioritized by obtaining from the registration center based on the topic, if not obtained, use this field to replace</td></tr></tbody></table>

**Request Example**:

```json
{
  "url": "http://127.0.0.1:8088/sub/test",
  "consumerGroup": "TEST-GROUP",
  "topic": [
    {
      "mode": "CLUSTERING",
      "topic": "TEST-TOPIC-HTTP-ASYNC",
      "type": "ASYNC"
    }
  ],
  "remoteMesh" : "http://127.0.0.1:10105/eventmesh/subscribe/local"
}
```

<a id="design-document-event-handling-and-integration-event-bridge--02-local-subscription"></a>

## 02 Local Subscription

**Description**: Initiates a local subscription command to cluster2 EventMesh. Upon receiving the subscription command, cluster2 EventMesh will start locally listening for messages received from Event Store and push them to the URL in the subscription information.

**URL**: http://{cluster2 address}/eventmesh/subscribe/local

**Request Method**: POST

**Request Parameters**: application/json format

<table><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>String</td><td>Yes</td><td>Identifies the subscription URL</td></tr><tr><td>consumerGroup</td><td>String</td><td>Yes</td><td>Identifies the consumer group information</td></tr><tr><td>topic</td><td>List</td><td>Yes</td><td>Identifies the subscription information list</td></tr><tr><td>mode</td><td>String</td><td>Yes</td><td>Identifies the consumption mode, divided into clustering mode and broadcast mode</td></tr><tr><td>topic</td><td>String</td><td>Yes</td><td>Identifies the subscribed topic</td></tr><tr><td>type</td><td>String</td><td>Yes</td><td>Identifies the consumption type, divided into synchronous and asynchronous</td></tr></tbody></table>

**Request Example**:

```JSON
{
  "url": "http://127.0.0.1:8088/sub/test",
  "consumerGroup": "TEST-GROUP",
  "topic": [
    {
      "mode": "CLUSTERING",
      "topic": "TEST-TOPIC-HTTP-ASYNC",
      "type": "ASYNC"
    }
  ]
}
```

<a id="design-document-event-handling-and-integration-event-bridge--03-send-message"></a>

## 03 Send Message

**Description**: Sends a message to cluster1 EventMesh. Upon receiving the message, cluster1 EventMesh will send it to Event Store, and then push the message received from Event Store to the URL `/eventmesh/bridge/publish` of cluster2 EventMesh.

**URL**: http://{cluster1 address}/eventmesh/publish/TEST-TOPIC-HTTP-ASYNC

**Request Method**: POST

**Request Parameters**: application/json format

**Request Example**:

```json
{
    "name":"test",
    "age":"19"
}
```

<a id="design-document-event-handling-and-integration-event-bridge--04-remote-unsubscribe"></a>

## 04 Remote Unsubscribe

**Description**: Sends an unsubscribe command to cluster2 EventMesh. Upon receiving the command, cluster2 EventMesh will send it to cluster1 EventMesh, and cluster1 EventMesh will locally execute the unsubscribe.

**URL**: http://{cluster2 address}/eventmesh/unsubscribe/remote

**Request Method**: POST

**Request Parameters**: application/json format

<table><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>String</td><td>Yes</td><td>Identifies the URL to unsubscribe, temporarily useless, will be replaced by (/eventmesh/bridge/publish) later, currently only for strong validation, will actually be replaced by the group information of cluster2 eventmesh</td></tr><tr><td>consumerGroup</td><td>String</td><td>Yes</td><td>Identifies the consumer group information to unsubscribe from, will use the group information of EventMesh cluster2 to replace</td></tr><tr><td>topic</td><td>List</td><td>Yes</td><td>Identifies the subscription topic information list</td></tr></tbody></table>

**Request Example**:

```json
{
  "consumerGroup": "EventMeshTest-consumerGroup",
  "url": "http://127.0.0.1:8088/sub/test",
  "topic": [
    "TEST-TOPIC-HTTP-ASYNC"
  ]
}
```

<a id="design-document-event-handling-and-integration-event-bridge--05-local-unsubscribe"></a>

## 05 Local Unsubscribe

**Description**: Sends an unsubscribe command to cluster2 EventMesh. Upon receiving the command, cluster2 EventMesh will locally execute the unsubscribe.

**URL**: http://{cluster2 address}/eventmesh/unsubscribe/local

**Request Method**: POST

**Request Parameters**: application/json format

<table><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>String</td><td>Yes</td><td>Identifies the URL to unsubscribe from</td></tr><tr><td>consumerGroup</td><td>String</td><td>Yes</td><td>Identifies the consumer group information to unsubscribe from</td></tr><tr><td>topic</td><td>List</td><td>Yes</td><td>Identifies the subscription topic information list</td></tr></tbody></table>

**Request Example**:

```json
{
  "consumerGroup": "EventMeshTest-consumerGroup",
  "url": "http://127.0.0.1:8088/sub/test",
  "topic": [
    "TEST-TOPIC-HTTP-ASYNC"
  ]
}
```

- [01 Remote Subscription](#design-document-event-handling-and-integration-event-bridge--01-remote-subscription)
- [02 Local Subscription](#design-document-event-handling-and-integration-event-bridge--02-local-subscription)
- [03 Send Message](#design-document-event-handling-and-integration-event-bridge--03-send-message)
- [04 Remote Unsubscribe](#design-document-event-handling-and-integration-event-bridge--04-remote-unsubscribe)
- [05 Local Unsubscribe](#design-document-event-handling-and-integration-event-bridge--05-local-unsubscribe)

---

<a id="design-document-event-handling-and-integration-webhook"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/event-handling-and-integration/webhook/ -->

<!-- page_index: 14 -->

# Use Webhook to subscribe events

Version: v1.12.0

# Use Webhook to subscribe events

<a id="design-document-event-handling-and-integration-webhook--webhook-usage-process"></a>

## Webhook usage process

<a id="design-document-event-handling-and-integration-webhook--the-first-step-configure-webhook-related-information-in-eventmesh-and-start"></a>

### The first step: Configure Webhook related information in EventMesh and start

Configuration:

```text
# Webhook HTTP payload listening port
eventMesh.server.http.port=10105
# Webhook config admin port
eventMesh.server.admin.http.port=10106

# Whether to start the Webhook admin service
eventMesh.webHook.admin.start=true

# Webhook event configuration storage mode. But currently only supports file and nacos
eventMesh.webHook.operationMode=file

# The file path of fileMode. If you write #{eventMeshHome}, in the eventMesh root directory
eventMesh.webHook.fileMode.filePath= #{eventMeshHome}/webhook

# The nacos storage mode. The configuration naming rule is eventMesh.webHook.nacosMode.{nacos native configuration key} For the specific configuration, please see [nacos github api](https://github.com/alibaba/nacos/blob/develop/api/src/main/java /com/alibaba/nacos/api/SystemPropertyKeyConst.java)
## address of nacos
eventMesh.webHook.nacosMode.serverAddr=127.0.0.1:8848

# Webhook CloudEvent sending mode. This property is the same as the eventMesh.storage.plugin.type configuration.
eventMesh.webHook.producer.connector=standalone
```

<a id="design-document-event-handling-and-integration-webhook--the-second-step-add-webhook-configuration-information"></a>

### The second step: Add Webhook configuration information

Configuration information description:

```java
   /**
    * The path called by the manufacturer. Manufacturer event call address, [http or https]://[domain or IP]:[port]/webhook/[callbackPath]
    * for example: http://127.0.0.1:10105/webhook/test/event , The full url needs to be filled in the manufacturer call input
    * callbackPath is the only
    */
    private String callbackPath;

    /**
     * manufacturer name, like github
     */
    private String manufacturerName;

    /**
     * manufacturer domain name, like www.github.com
     */
    private String manufacturerDomain;

    /**
     * Webhook event name, like rep-push
     */
    private String manufacturerEventName;

    /**
     * http header content type
     */
    private String contentType = "application/json";

    /**
     * description of this WebHookConfig
     */
    private String description;

    /**
     * secret key, for authentication
     */
    private String secret;

    /**
     * userName, for HTTP authentication
     */
    private String userName;

    /**
     * password, for HTTP authentication
     */
    private String password;

    /**
     * roll out event name, like topic to mq
     */
    private String cloudEventName;

    /**
     * roll out data format -> CloudEvent serialization mode
     * If HTTP protocol is used, the request header contentType needs to be marked
     */
    private String dataContentType = "application/json";

    /**
     * id of cloudEvent, like uuid/manufacturerEventId
     */
    private String cloudEventIdGenerateMode;
```

<a id="design-document-event-handling-and-integration-webhook--add-webhook-config"></a>

#### Add WebHook config

path: /webhook/insertWebHookConfig

method: POST

contentType: application/json

input params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>callbackPath</td><td>call address, unique address</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerName</td><td>manufacturer name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerDomain</td><td>manufacturer domain name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerEventName</td><td>manufacturer event name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>contentType</td><td>http connettype</td><td>string</td><td>N</td><td>application/json</td></tr><tr><td>description</td><td>configuration instructions</td><td>string</td><td>N</td><td>null</td></tr><tr><td>secret</td><td>signature string</td><td>string</td><td>N</td><td>null</td></tr><tr><td>userName</td><td>username</td><td>string</td><td>N</td><td>null</td></tr><tr><td>password</td><td>password</td><td>string</td><td>N</td><td>null</td></tr><tr><td>cloudEventName</td><td>cloudEvent name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>cloudEventIdGenerateMode</td><td>cloudEvent event object identification method, uuid or event id</td><td>string</td><td>N</td><td>manufacturerEventId</td></tr></tbody></table>

E.g:

```json
{
    "callbackPath":"/webhook/github/eventmesh/all",
    "manufacturerName":"github",
    "manufacturerDomain":"www.github.com",
    "manufacturerEventName":"all",
    "cloudEventName":"github-eventmesh"
}
```

Output params: 1 for success, 0 for failure

<a id="design-document-event-handling-and-integration-webhook--query-webhook-config-by-callback-path"></a>

#### Query WebHook config by callback path

path: /webhook/queryWebHookConfigById

method: POST

contentType： application/json

input params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>callbackPath</td><td>call address, unique address</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerName</td><td>the caller of this callbackPath belongs to</td><td>string</td><td>Y</td><td>null</td></tr></tbody></table>

E.g:

```json
{
    "callbackPath":"/webhook/github/eventmesh/all",
    "manufacturerName":"github"
}
```

Output params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>callbackPath</td><td>call address, unique address</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerName</td><td>manufacturer name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerDomain</td><td>manufacturer domain name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerEventName</td><td>manufacturer event name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>contentType</td><td>http connettype</td><td>string</td><td>N</td><td>application/json</td></tr><tr><td>description</td><td>configuration instructions</td><td>string</td><td>N</td><td>null</td></tr><tr><td>secret</td><td>signature key</td><td>string</td><td>N</td><td>null</td></tr><tr><td>userName</td><td>user name</td><td>string</td><td>N</td><td>null</td></tr><tr><td>password</td><td>password</td><td>string</td><td>N</td><td>null</td></tr><tr><td>cloudEventName</td><td>cloudEvent name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>cloudEventIdGenerateMode</td><td>cloudEvent event object identification method, uuid or event id</td><td>string</td><td>N</td><td>manufacturerEventId</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-webhook--query-webhook-config-by-manufacturer"></a>

#### Query WebHook config by manufacturer

path: /webhook/queryWebHookConfigByManufacturer

method: POST

contentType： application/json

input params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>manufacturerName</td><td>manufacturer name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>pageNum</td><td>page number of paging query</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>pageSize</td><td>page size of each page</td><td>string</td><td>Y</td><td>null</td></tr></tbody></table>

E.g:

```json
{
    "manufacturerName":"github",
    "pageNum":1,
    "pageSize":2
}
```

Output params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>callbackPath</td><td>call address, unique address</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerName</td><td>manufacturer name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerDomain</td><td>manufacturer domain name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerEventName</td><td>manufacturer event name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>contentType</td><td>http connettype</td><td>string</td><td>N</td><td>application/json</td></tr><tr><td>description</td><td>configuration instructions</td><td>string</td><td>N</td><td>null</td></tr><tr><td>secret</td><td>signature key</td><td>string</td><td>N</td><td>null</td></tr><tr><td>userName</td><td>user name</td><td>string</td><td>N</td><td>null</td></tr><tr><td>password</td><td>password</td><td>string</td><td>N</td><td>null</td></tr><tr><td>cloudEventName</td><td>cloudEvent name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>cloudEventIdGenerateMode</td><td>cloudEvent event object identification method, uuid or event id</td><td>string</td><td>N</td><td>manufacturerEventId</td></tr></tbody></table>
<a id="design-document-event-handling-and-integration-webhook--update-webhook-config"></a>

#### Update WebHook config

path: /webhook/updateWebHookConfig

method: POST

contentType: application/json

input params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>callbackPath</td><td>call address, unique address</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerName</td><td>manufacturer name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerDomain</td><td>manufacturer domain name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerEventName</td><td>manufacturer event name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>contentType</td><td>http connettype</td><td>string</td><td>N</td><td>application/json</td></tr><tr><td>description</td><td>configuration instructions</td><td>string</td><td>N</td><td>null</td></tr><tr><td>secret</td><td>signature string</td><td>string</td><td>N</td><td>null</td></tr><tr><td>userName</td><td>username</td><td>string</td><td>N</td><td>null</td></tr><tr><td>password</td><td>password</td><td>string</td><td>N</td><td>null</td></tr><tr><td>cloudEventName</td><td>cloudEvent name</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>cloudEventIdGenerateMode</td><td>cloudEvent event object identification method, uuid or event id</td><td>string</td><td>N</td><td>manufacturerEventId</td></tr></tbody></table>

E.g:

```json
{
    "callbackPath":"/webhook/github/eventmesh/all",
    "manufacturerName":"github",
    "manufacturerDomain":"www.github.com",
    "manufacturerEventName":"all",
    "cloudEventName":"github-eventmesh"
}
```

Output params: 1 for success, 0 for failure

<a id="design-document-event-handling-and-integration-webhook--delete-webhook-config"></a>

#### Delete WebHook config

path: /webhook/deleteWebHookConfig

method: POST

contentType： application/json

input params:

<table><thead><tr><th>field</th><th>desc</th><th>type</th><th>necessary</th><th>default</th></tr></thead><tbody><tr><td>callbackPath</td><td>call address, unique address</td><td>string</td><td>Y</td><td>null</td></tr><tr><td>manufacturerName</td><td>the caller of this callbackPath belongs to</td><td>string</td><td>Y</td><td>null</td></tr></tbody></table>

E.g:

```json
{
    "callbackPath":"/webhook/github/eventmesh/all",
    "manufacturerName":"github"
}
```

Output params: 1 for success, 0 for failure

<a id="design-document-event-handling-and-integration-webhook--the-third-step-check-if-the-configuration-is-successful"></a>

### The third step: Check if the configuration is successful

1. file storage mode. Please go to the eventMesh.webHook.fileMode.filePath directory to view. The Filename is callbackPath.
2. nacos storage mode. Please go to the nacos service configured by eventMesh.webHook.nacosMode.serverAddr to see this.

<a id="design-document-event-handling-and-integration-webhook--the-fourth-step-configure-the-consumer-of-cloudevent"></a>

### The fourth step: Configure the consumer of cloudevent

<a id="design-document-event-handling-and-integration-webhook--the-fifth-step-configure-webhook-related-information-in-the-manufacturer"></a>

### The fifth step: Configure Webhook related information in the manufacturer

> For manufacturer's operation, please refer to [Manufacturer's Webhook operation instructions](#design-document-event-handling-and-integration-webhook--manufacturer-s-webhook-operation-instructions).

<a id="design-document-event-handling-and-integration-webhook--manufacturers-webhook-operation-instructions"></a>

## Manufacturer's Webhook operation instructions

<a id="design-document-event-handling-and-integration-webhook--github-sign-up"></a>

### GitHub sign up

<a id="design-document-event-handling-and-integration-webhook--the-first-step-enter-the-corresponding-project"></a>

#### The first step: Enter the corresponding project

<a id="design-document-event-handling-and-integration-webhook--the-second-step-click-setting"></a>

#### The second step: click setting

![](assets/images/webhook-github-setting-27fa2024d0625a7443957776ecbc7e3a_a4a26bd124a5636f.png)

<a id="design-document-event-handling-and-integration-webhook--the-third-step-click-webhooks"></a>

#### The third step: click Webhooks

![](assets/images/webhook-github-webhooks-8f08530fcf0f98859e5d1697049eec18_9b5d63066917a42d.png)

<a id="design-document-event-handling-and-integration-webhook--the-fourth-step-click-on-add-webhook"></a>

#### The fourth step: Click on Add Webhook

![](assets/images/webhook-github-add-185bf8d63c1b465e206bfe7deabd43fc_fd681d40a4067ba5.png)

<a id="design-document-event-handling-and-integration-webhook--the-fifth-step-fill-in-the-webhook-information"></a>

#### The fifth step: Fill in the Webhook information

![](assets/images/webhook-github-info-aabfbb67a9dcdc908674b880bc087780_440e8c83fdce91c6.png)

Payload URL: EventMesh service address and callbackPath, which must include the protocol header. For example, when the callback address `callbackPath` is `/webhook/github/eventmesh/all`, the Payload URL is `http://www.example.com:10105/webhook/github/eventmesh/all`.

[http or https]://[domain or IP]:[port]/webhook/[callbackPath]

Content type: http header content type

Secret: signature string

- [Webhook usage process](#design-document-event-handling-and-integration-webhook--webhook-usage-process)
  - [The first step: Configure Webhook related information in EventMesh and start](#design-document-event-handling-and-integration-webhook--the-first-step-configure-webhook-related-information-in-eventmesh-and-start)
  - [The second step: Add Webhook configuration information](#design-document-event-handling-and-integration-webhook--the-second-step-add-webhook-configuration-information)
  - [The third step: Check if the configuration is successful](#design-document-event-handling-and-integration-webhook--the-third-step-check-if-the-configuration-is-successful)
  - [The fourth step: Configure the consumer of cloudevent](#design-document-event-handling-and-integration-webhook--the-fourth-step-configure-the-consumer-of-cloudevent)
  - [The fifth step: Configure Webhook related information in the manufacturer](#design-document-event-handling-and-integration-webhook--the-fifth-step-configure-webhook-related-information-in-the-manufacturer)
- [Manufacturer's Webhook operation instructions](#design-document-event-handling-and-integration-webhook--manufacturers-webhook-operation-instructions)
  - [GitHub sign up](#design-document-event-handling-and-integration-webhook--github-sign-up)

---

<a id="design-document-event-handling-and-integration-workflow"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/event-handling-and-integration/workflow/ -->

<!-- page_index: 15 -->

# EventMesh Workflow

Version: v1.12.0

# EventMesh Workflow

<a id="design-document-event-handling-and-integration-workflow--business-problem"></a>

## Business Problem

Imaging you are building a simple Order Management System for an E-Commerce Store. The system should be able to receive and provision new orders from a store website. The provisioning process should be able to process all orders, handle payments, as well as process shipments.

For high availability and high performance, you architect the system using event-driven architecture (EDA), and build microservice apps to handle store frontend, order management, payment processing, and shipment management. You deploy the whole system in a cloud environment. To handle high workloads, you leverage a messaging system to buffer the loads, and scale up multiple instances of microservices. The architecture could look similar to:

![Workflow Use Case](assets/images/workflow-use-case-33b55ea03d6330c426b62a8164e6e23c_2dbfd96c2435dd69.jpg)

While each microservice is acting on its own event channels, EventMesh plays a crucial role of doing Event Orchestration.

We use [CNCF Serverless Workflow](https://serverlessworkflow.io/) to describe this Event Workflow Orchestration.

<a id="design-document-event-handling-and-integration-workflow--cncf-serverless-workflow"></a>

## CNCF Serverless Workflow

CNCF Serverless Workflow defines a vendor-neutral, open-source, and fully community-driven ecosystem for defining and running DSL-based workflows that target the Serverless technology domain.

Serverless Workflow defines a Domain Specific Language (DSL) to describe stateful and stateless workflow-based orchestrations of serverless functions and microservices.

More details could be found in its [official github site](https://github.com/serverlessworkflow/specification)

<a id="design-document-event-handling-and-integration-workflow--eventmesh-workflow-1"></a>

## EventMesh Workflow

We leverage Serverless Workflow DSL to describe the EventMesh workflow. Based on its spec, the workflow is consists of a series of workflow states used to describe the control-flow logic. At this time we only support event related workflow states. See the supported states in [Workflow DSL Design](#design-document-event-handling-and-integration-workflow--workflow-dsl-design-wip).

A `workflow state` can include applicable `actions`, or services/functions that should be invoked during workflow execution. These `actions` can reference reusable `function` definitions which define how these functions/services should be invoked. They can also reference events that trigger event-based service invocations, and events to wait for that denote completion of such event-based service invocation completion.

In EDA solution, we usually defined our event-driven microservice using AsyncAPI. Serverless workflow `function` definitions support defining invocation semantics using AsyncAPI. See [Using Funtions for AsyncAPI Service](https://github.com/serverlessworkflow/specification/blob/main/specification.md#using-functions-for-async-api-service-invocations) for more information.

<a id="design-document-event-handling-and-integration-workflow--asyncapi"></a>

### AsyncAPI

AsyncAPI is an open source initiative that seeks to improve the current state of Event-Driven Architectures (EDA).
Our long-term goal is to make working with EDAs as easy as it is to work with REST APIs.
That goes from documentation to code generation, discovery to event management.
Most of the processes you apply to your REST APIs nowadays would be applicable to your event-driven/asynchronous APIs too.

See AsyncAPI detail in the [official site](https://www.asyncapi.com/docs/guides)

<a id="design-document-event-handling-and-integration-workflow--workflow-example"></a>

### Workflow Example

In this example, we build the event-driven workflow of the Order management system above.

First, we need to define AsyncAPI definitions for our microservice apps.

- Online Store App

```yaml
asyncapi: 2.2.0
info:
  title: Online Store application
  version: '0.1.0'
channels:
  store/order:
    subscribe:
      operationId: newStoreOrder
      message:
        $ref : '#/components/NewOrder'
```

- Order Service

```yaml
asyncapi: 2.2.0
info:
  title: Order Service
  version: '0.1.0'
channels:
  order/inbound:
    publish:
      operationId: sendOrder
      message:
        $ref : '#/components/Order'
  order/outbound:
    subscribe:
      operationId: processedOrder
      message:
        $ref : '#/components/Order'
```

- Payment Service

```yaml
asyncapi: 2.2.0
info:
  title: Payment Service
  version: '0.1.0'
channels:
  payment/inbound:
    publish:
      operationId: sendPayment
      message:
        $ref : '#/components/OrderPayment'
  payment/outbound:
    subscribe:
      operationId: paymentReceipt
      message:
        $ref : '#/components/OrderPayment'
```

- Shipment Service

```yaml
asyncapi: 2.2.0
info:
  title: Shipment Service
  version: '0.1.0'
channels:
  shipment/inbound:
    publish:
      operationId: sendShipment
      message:
        $ref : '#/components/OrderShipment'
```

Once that is defined, we define the order workflow that describes our Order Management business logic.

```yaml
id: storeorderworkflow
version: '1.0'
specVersion: '0.8'
name: Store Order Management Workflow
states:
  - name: Receive New Order Event
    type: event
    onEvents:
      - eventRefs:
          - NewOrderEvent
        actions:
          - eventRef:
              triggerEventRef: OrderServiceSendEvent
              resultEventRef: OrderServiceResultEvent
          - eventRef:
              triggerEventRef: PaymentServiceSendEvent
              resultEventRef: PaymentServiceResultEvent
    transition: Check Payment Status
  - name: Check Payment Status
    type: switch
    dataConditions:
      - name: Payment Successfull
        condition: "${ .payment.status == 'success' }"
        transition: Send Order Shipment
      - name: Payment Denied
        condition: "${ .payment.status == 'denied' }"
        end: true
    defaultCondition:
      end: true
  - name: Send Order Shipment
    type: operation
    actions:
      - eventRef:
          triggerEventRef: ShipmentServiceSendEvent
    end: true
events:
  - name: NewOrderEvent
    source: file://onlineStoreApp.yaml#newStoreOrder
    type: asyncapi
    kind: consumed
  - name: OrderServiceSendEvent
    source: file://orderService.yaml#sendOrder
    type: asyncapi
    kind: produced
  - name: OrderServiceResultEvent
    source: file://orderService.yaml#processedOrder
    type: asyncapi
    kind: consumed
  - name: PaymentServiceSendEvent
    source: file://paymentService.yaml#sendPayment
    type: asyncapi
    kind: produced
  - name: PaymentServiceResultEvent
    source: file://paymentService.yaml#paymentReceipt
    type: asyncapi
    kind: consumed
  - name: ShipmentServiceSendEvent
    source: file://shipmentService.yaml#sendShipment
    type: asyncapi
    kind: produced
```

The corresponding workflow diagram is the following:

![Workflow Diagram](assets/images/workflow-diagram-705cf9a6d5c8a5c3b465cba0a216f2a4_57c27da972bacdfb.png)

<a id="design-document-event-handling-and-integration-workflow--eventmesh-workflow-engine"></a>

## EventMesh Workflow Engine

In the following architecture diagram, the EventMesh Catalog, EventMesh Workflow Engine and EventMesh Runtime are running in three different processors.

![Workflow Architecture](assets/images/workflow-architecture-cf4b8c8a7aaa33bb0ffaf1db4cf9cb52_fffe60bda655398e.jpg)

The steps running the workflow is the followings:

1. Deploy the Publisher and Subscriber Apps in the environment.
   Describe the App APIs using AsyncAPI, generate the asyncAPI yaml.
   Register the Publisher and Subscriber Apps in EventMesh Catalog using AsyncAPI.
2. Register the Serverless Workflow DSL in EventMesh Workflow Engine.
3. EventMesh Workflow Engine query the EventMesh Catalog for Publisher and Subscribers required in Workflow DSL `function`
4. Event-driven Apps are publish events to EventMesh Runtime to trigger the Workflow. EventMesh Workflow Engine also publish and subscribe events for orchestrating the events.

<a id="design-document-event-handling-and-integration-workflow--eventmesh-catalog-design"></a>

### EventMesh Catalog Design

EventMesh Catalog store the Publisher, Subscriber and Channel metadata. consists of the following modules:

- AsyncAPI Parser

  Using the SDK provided by AsyncAPI community (see [tool list](https://www.asyncapi.com/docs/community/tooling)),
  parse and validated the AsyncAPI yaml inputs, and generate the AsyncAPI definition.
- Publisher, Channel, Subscriber Modules

  From the AsyncAPI definition store the Publisher, Subscriber and Channel information.

<a id="design-document-event-handling-and-integration-workflow--eventmesh-workflow-engine-design"></a>

### EventMesh Workflow Engine Design

EventMesh Workflow Engine consists of the following modules:

- Workflow Parser

  Using the SDK provided by Serverless Workflow community (see supported [SDKs](https://github.com/serverlessworkflow/specification#sdks)),
  parse and validated the workflow DSL inputs, and generate workflow definition.
- Workflow Module

  It manages a workflow instance life cycle, from create, start, stop to destroy.
- State Module

  It manages workflow state life cycle. We support the event-related states, and the supported state list below is Work-in-Progress.

  <table><thead><tr><th>Workflow State</th><th>Description</th></tr></thead><tbody><tr><td>Operation</td><td>Execute the AsyncAPI functions defined in the Actions</td></tr><tr><td>Event</td><td>Check if the defined Event matched, if so execute the defined AsyncAPI functions</td></tr><tr><td>Switch</td><td>Check the event is matched with the event-conditions, and execute teh defined AsyncAPI functions</td></tr><tr><td>Parallel</td><td>Execute the defined AsyncAPI functions in parallel</td></tr><tr><td>ForEach</td><td>Iterate the inputCollection and execute the defined AsyncAPI functions</td></tr></tbody></table>
- Action Module

  It managed the functions inside the action.
- Function Module

  It manages the AsyncAPI functions by creating the publisher and/or subscriber in EventMesh Runtime, and manage the publisher/subscriber life cycle.

  <table><thead><tr><th>AsyncAPI Operation</th><th>EventMesh Runtime</th></tr></thead><tbody><tr><td>Publish</td><td>Publisher</td></tr><tr><td>Subscribe</td><td>Subscriber</td></tr></tbody></table>
- Event Module

  It manages the CloudEvents data model, including event filter, correlation and transformation using the rules defined in the workflow DSL.
- Retry Module

  It manages the retry logic of the event publishing into EventMesh Runtime.

- [Business Problem](#design-document-event-handling-and-integration-workflow--business-problem)
- [CNCF Serverless Workflow](#design-document-event-handling-and-integration-workflow--cncf-serverless-workflow)
- [EventMesh Workflow](#design-document-event-handling-and-integration-workflow--eventmesh-workflow-1)
  - [AsyncAPI](#design-document-event-handling-and-integration-workflow--asyncapi)
  - [Workflow Example](#design-document-event-handling-and-integration-workflow--workflow-example)
- [EventMesh Workflow Engine](#design-document-event-handling-and-integration-workflow--eventmesh-workflow-engine)
  - [EventMesh Catalog Design](#design-document-event-handling-and-integration-workflow--eventmesh-catalog-design)
  - [EventMesh Workflow Engine Design](#design-document-event-handling-and-integration-workflow--eventmesh-workflow-engine-design)

---

<a id="design-document-observability-metrics-export"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/observability/metrics-export/ -->

<!-- page_index: 16 -->

# EventMesh Metrics (OpenTelemetry and Prometheus)

Version: v1.12.0

# EventMesh Metrics (OpenTelemetry and Prometheus)

<a id="design-document-observability-metrics-export--introduction"></a>

## Introduction

[EventMesh](https://github.com/apache/eventmesh) is a dynamic cloud-native eventing infrastructure.

<a id="design-document-observability-metrics-export--an-overview-of-opentelemetry"></a>

## An overview of OpenTelemetry

OpenTelemetry is a collection of tools, APIs, and SDKs. You can use it to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) for analysis in order to understand your software's performance and behavior.

<a id="design-document-observability-metrics-export--an-overview-of-prometheus"></a>

## An overview of Prometheus

Power your metrics and alerting with a leading open-source monitoring solution.

- Dimensional data
- Powerful queries
- Great visualization
- Efficient storage
- Simple operation
- Precise alerting
- Many client libraries
- Many integrations

<a id="design-document-observability-metrics-export--requirements"></a>

## Requirements

<a id="design-document-observability-metrics-export--functional-requirements"></a>

### Functional Requirements

<table><thead><tr><th align="left">Requirement ID</th><th>Requirement Description</th><th>Comments</th></tr></thead><tbody><tr><td align="left">F-1</td><td>EventMesh users should be able to observe HTTP metrics from Prometheus</td><td>Functionality</td></tr><tr><td align="left">F-2</td><td>EventMesh users should be able to observe TCP metrics from Prometheus</td><td>Functionality</td></tr></tbody></table>
<a id="design-document-observability-metrics-export--design-details"></a>

## Design Details

use the meter instrument provided by OpenTelemetry to observe the metrics exist in EventMesh then export to Prometheus.

1. Initialize a meter instrument
2. set the Prometheus server
3. different metrics observer built

<a id="design-document-observability-metrics-export--appendix"></a>

## Appendix

<a id="design-document-observability-metrics-export--references"></a>

### References

<https://github.com/open-telemetry/docs-cn/blob/main/QUICKSTART.md#%E5%88%9B%E5%BB%BA%E5%9F%BA%E7%A1%80Span>

- [Introduction](#design-document-observability-metrics-export--introduction)
- [An overview of OpenTelemetry](#design-document-observability-metrics-export--an-overview-of-opentelemetry)
- [An overview of Prometheus](#design-document-observability-metrics-export--an-overview-of-prometheus)
- [Requirements](#design-document-observability-metrics-export--requirements)
  - [Functional Requirements](#design-document-observability-metrics-export--functional-requirements)
- [Design Details](#design-document-observability-metrics-export--design-details)
- [Appendix](#design-document-observability-metrics-export--appendix)
  - [References](#design-document-observability-metrics-export--references)

---

<a id="design-document-observability-tracing"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/observability/tracing/ -->

<!-- page_index: 17 -->

# Distributed Tracing

Version: v1.12.0

# Distributed Tracing

<a id="design-document-observability-tracing--overview-of-opentelemetry"></a>

## Overview of OpenTelemetry

OpenTelemetry is a collection of tools, APIs, and SDKs. You can use it to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) for analysis in order to understand your software's performance and behavior.

<a id="design-document-observability-tracing--requirements"></a>

## Requirements

- set tracer
- different exporter
- start and end span in server

<a id="design-document-observability-tracing--design-details"></a>

## Design Details

- SpanProcessor: BatchSpanProcessor
- Exporter: log(default), would be changed from properties

```java
// Configure the batch spans processor. This span processor exports span in batches.
BatchSpanProcessor batchSpansProcessor =
    BatchSpanProcessor.builder(exporter)
        .setMaxExportBatchSize(512) // set the maximum batch size to use
        .setMaxQueueSize(2048) // set the queue size. This must be >= the export batch size
        .setExporterTimeout(
            30, TimeUnit.SECONDS) // set the max amount of time an export can run before getting
        // interrupted
        .setScheduleDelay(5, TimeUnit.SECONDS) // set time between two different exports
        .build();
OpenTelemetrySdk.builder()
    .setTracerProvider(
        SdkTracerProvider.builder().addSpanProcessor(batchSpansProcessor).build())
    .build();
```

1. When using the method 'init()' of the class "EventMeshHTTPServer", the class "AbstractHTTPServer” will get the tracer

```java
super.openTelemetryTraceFactory = new OpenTelemetryTraceFactory(eventMeshHttpConfiguration);
super.tracer = openTelemetryTraceFactory.getTracer(this.getClass().toString());
super.textMapPropagator = openTelemetryTraceFactory.getTextMapPropagator();
```

2. then the trace in class "AbstractHTTPServer” will work.

<a id="design-document-observability-tracing--problems"></a>

## Problems

<a id="design-document-observability-tracing--how-to-set-different-exporter-in-class-opentelemetrytracefactory-solved"></a>

### How to set different exporter in class 'OpenTelemetryTraceFactory'? (Solved)

After I get the exporter type from properties, how to deal with it.

The 'logExporter' only needs to new it.

But the 'zipkinExporter' needs to new and use the "getZipkinExporter()" method.

<a id="design-document-observability-tracing--solutions"></a>

## Solutions

<a id="design-document-observability-tracing--solution-of-different-exporter"></a>

### Solution of different exporter

Use reflection to get an exporter.

First of all, different exporter must implement the interface 'EventMeshExporter'.

Then we get the exporter name from the configuration and reflect to the class.

```java
//different spanExporter
String exporterName = configuration.eventMeshTraceExporterType;
//use reflection to get spanExporter
String className = String.format("org.apache.eventmesh.runtime.exporter.%sExporter",exporterName);
EventMeshExporter eventMeshExporter = (EventMeshExporter) Class.forName(className).newInstance();
spanExporter = eventMeshExporter.getSpanExporter(configuration);
```

Additional, this will surround with try catch.If the specified exporter cannot be obtained successfully, the default exporter log will be used instead

<a id="design-document-observability-tracing--improvement-of-different-exporter"></a>

#### Improvement of different exporter

SPI (To be completed)

<a id="design-document-observability-tracing--appendix"></a>

## Appendix

<a id="design-document-observability-tracing--references"></a>

### References

<https://github.com/open-telemetry/docs-cn/blob/main/QUICKSTART.md>

<https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/netty>

- [Overview of OpenTelemetry](#design-document-observability-tracing--overview-of-opentelemetry)
- [Requirements](#design-document-observability-tracing--requirements)
- [Design Details](#design-document-observability-tracing--design-details)
- [Problems](#design-document-observability-tracing--problems)
  - [How to set different exporter in class 'OpenTelemetryTraceFactory'? (Solved)](#design-document-observability-tracing--how-to-set-different-exporter-in-class-opentelemetrytracefactory-solved)
- [Solutions](#design-document-observability-tracing--solutions)
  - [Solution of different exporter](#design-document-observability-tracing--solution-of-different-exporter)
- [Appendix](#design-document-observability-tracing--appendix)
  - [References](#design-document-observability-tracing--references)

---

<a id="design-document-observability-prometheus"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/observability/prometheus/ -->

<!-- page_index: 18 -->

# Observe Metrics with Prometheus

Version: v1.12.0

# Observe Metrics with Prometheus

<a id="design-document-observability-prometheus--prometheus"></a>

## Prometheus

[Prometheus](https://prometheus.io/docs/introduction/overview/) is an open-source system monitoring and alerting toolkit that collects and stores the metrics as time-series data. EventMesh exposes a collection of metrics data that could be scraped and analyzed by Prometheus. Please follow [the "First steps with Prometheus" tutorial](https://prometheus.io/docs/introduction/first_steps/) to download and install the latest release of Prometheus.

<a id="design-document-observability-prometheus--edit-prometheus-configuration"></a>

## Edit Prometheus Configuration

The `eventmesh-runtime/conf/prometheus.yml` configuration file specifies the port of the metrics HTTP endpoint. The default metrics port is `19090`.

```properties
eventMesh.metrics.prometheus.port=19090
```

Please refer to [the Prometheus configuration guide](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) to add the EventMesh metrics as a scrape target in the configuration file. Here's the minimum configuration that creates a job with the name `eventmesh` and the endpoint `http://localhost:19090`:

```yaml
scrape_configs:
  - job_name: "eventmesh"
    static_configs:
      - targets: ["localhost:19090"]
```

Please navigate to the Prometheus dashboard (e.g. `http://localhost:9090`) to view the list of metrics exported by EventMesh, which are prefixed with `eventmesh_`.

- [Prometheus](#design-document-observability-prometheus--prometheus)
- [Edit Prometheus Configuration](#design-document-observability-prometheus--edit-prometheus-configuration)

---

<a id="design-document-observability-zipkin"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/observability/zipkin/ -->

<!-- page_index: 19 -->

# Collect Trace with Zipkin

Version: v1.12.0

# Collect Trace with Zipkin

<a id="design-document-observability-zipkin--zipkin"></a>

## Zipkin

Distributed tracing is a method used to profile and monitor applications built with microservices architecture. Distributed tracing helps pinpoint where failures occur and what causes poor performance.

[Zipkin](https://zipkin.io) is a distributed tracing system that helps collect timing data needed to troubleshoot latency problems in service architectures. EventMesh exposes a collection of trace data that could be collected and analyzed by Zipkin. Please follow [the "Zipkin Quickstart" tutorial](https://zipkin.io/pages/quickstart.html) to download and install the latest release of Zipkin.

<a id="design-document-observability-zipkin--configuration"></a>

## Configuration

To enable the trace exporter of EventMesh Runtime, set the `eventMesh.server.trace.enabled` field in the `conf/eventmesh.properties` file to `true`.

```properties
# Trace plugin
eventMesh.server.trace.enabled=true
eventMesh.trace.plugin=zipkin
```

To customize the behavior of the trace exporter such as timeout or export interval, edit the `exporter.properties` file.

```properties
# Set the maximum batch size to use
eventmesh.trace.max.export.size=512
# Set the queue size. This must be >= the export batch size
eventmesh.trace.max.queue.size=2048
# Set the max amount of time an export can run before getting(TimeUnit=SECONDS)
eventmesh.trace.export.timeout=30
# Set time between two different exports (TimeUnit=SECONDS)
eventmesh.trace.export.interval=5
```

To send the exported trace data to Zipkin, edit the `eventmesh.trace.zipkin.ip` and `eventmesh.trace.zipkin.port` fields in the `conf/zipkin.properties` file to match the configuration of the Zipkin server.

```properties
# Zipkin's IP and Port
eventmesh.trace.zipkin.ip=localhost
eventmesh.trace.zipkin.port=9411
```

- [Zipkin](#design-document-observability-zipkin--zipkin)
- [Configuration](#design-document-observability-zipkin--configuration)

---

<a id="design-document-observability-jaeger"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/observability/jaeger/ -->

<!-- page_index: 20 -->

# Collect Trace with Jaeger

Version: v1.12.0

# Collect Trace with Jaeger

<a id="design-document-observability-jaeger--jaeger"></a>

## Jaeger

[Jaeger](https://www.jaegertracing.io/), inspired by [Dapper](https://research.google.com/pubs/pub36356.html) and [OpenZipkin](https://zipkin.io/), is a distributed tracing platform created by [Uber Technologies](https://uber.github.io/) and donated to [Cloud Native Computing Foundation](https://cncf.io/). It can be used for monitoring microservices-based distributed systems.

For the installation of Jaeger, you can refer to the [official documentation](https://www.jaegertracing.io/docs/latest/getting-started/) of Jaeger. It is recommended to use docker image `jaegertracing/all-in-one` to quickly build the environment for testing.

<a id="design-document-observability-jaeger--configuration"></a>

## Configuration

To enable the trace exporter of EventMesh Runtime, set the `eventMesh.server.trace.enabled` field in the `conf/eventmesh.properties` file to `true`.

```properties
# Trace plugin
eventMesh.server.trace.enabled=true
eventMesh.trace.plugin=jaeger
```

To customize the behavior of the trace exporter such as timeout or export interval, edit the `exporter.properties` file.

```properties
# Set the maximum batch size to use
eventmesh.trace.max.export.size=512
# Set the queue size. This must be >= the export batch size
eventmesh.trace.max.queue.size=2048
# Set the max amount of time an export can run before getting(TimeUnit=SECONDS)
eventmesh.trace.export.timeout=30
# Set time between two different exports (TimeUnit=SECONDS)
eventmesh.trace.export.interval=5
```

To send the exported trace data to Jaeger, edit the `eventmesh.trace.jaeger.ip` and `eventmesh.trace.jaeger.port` fields in the `conf/jaeger.properties` file to match the configuration of the Jaeger server.

```properties
# Jaeger's IP and Port
eventmesh.trace.jaeger.ip=localhost
eventmesh.trace.jaeger.port=14250
```

<a id="design-document-observability-jaeger--migrating-from-zipkin"></a>

## Migrating from Zipkin

Collector service exposes Zipkin compatible REST API `/api/v1/spans` which accepts both Thrift and JSON. Also there is `/api/v2/spans` for JSON and Proto.

So you can also use the `eventmesh-trace-zipkin` plugin to collect trace with Jaeger. Please refer to the `eventmesh-trace-zipkin` documentation for the specific configuration. By default this feature in Jaeger is disabled. It can be enabled with `--collector.zipkin.host-port=:9411`.

- [Jaeger](#design-document-observability-jaeger--jaeger)
- [Configuration](#design-document-observability-jaeger--configuration)
- [Migrating from Zipkin](#design-document-observability-jaeger--migrating-from-zipkin)

---

<a id="design-document-connect-connectors"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/connectors/ -->

<!-- page_index: 21 -->

# Connectors

Version: v1.12.0

# Connectors

<a id="design-document-connect-connectors--connector"></a>

## Connector

A connector is an image or instance that interacts with a specific external service or underlying data source (e.g., Databases) on behalf of user applications. A connector is either a Source or a Sink.

Connector runs as a standalone service by `main()`.

<a id="design-document-connect-connectors--source"></a>

## Source

A source connector obtains data from an underlying data producer, and delivers it to targets after original data has been transformed into CloudEvents. It doesn't limit the way how a source retrieves data. (e.g., A source may pull data from a message queue or act as an HTTP server waiting for data sent to it).

<a id="design-document-connect-connectors--sink"></a>

## Sink

A sink connector receives CloudEvents and does some specific business logics. (e.g., A MySQL Sink extracts useful data from CloudEvents and writes them to a MySQL database).

<a id="design-document-connect-connectors--cloudevents"></a>

## CloudEvents

A specification for describing event data in common formats to provide interoperability across services, platforms and systems.

<a id="design-document-connect-connectors--implements"></a>

## Implements

Add a new connector by implementing the source/sink interface using [eventmesh-openconnect-java](https://github.com/apache/eventmesh/tree/master/eventmesh-openconnect/eventmesh-openconnect-java).

<a id="design-document-connect-connectors--technical-solution"></a>

## Technical Solution

<a id="design-document-connect-connectors--structure-and-process"></a>

### Structure and process

![source-sink connector architecture](assets/images/connector-architecture-8dbcfb90423a11d295a275d9ef8e6774_6b1d90657d0fc5c9.png)

<a id="design-document-connect-connectors--design-detail"></a>

### Design Detail

![eventmesh-connect-detail](assets/images/connector-design-detail-f20f6c65bc25ddb811491080c71b1cea_9bc4ab784880d761.png)

<a id="design-document-connect-connectors--description"></a>

### Description

<a id="design-document-connect-connectors--worker"></a>

#### Worker

Worker is divided into Source Worker and Sink Worker, which are triggered by the `Application` class and implement the methods of the `ConnectorWorker` interface respectively, which include the worker's running life cycle, and the worker carries the running of the connector. Workers can be lightweight and independent through mirroring Running, the eventmesh-sdk-java module is integrated internally, and the CloudEvents protocol is used to interact with EventMesh. Currently, the TCP client is used by default. In the future, support for dynamic configuration can be considered.

<a id="design-document-connect-connectors--connector-1"></a>

#### Connector

Connectors are divided into Source Connector and Sink Connector. Connectors have their own configuration files and run independently. Workers perform reflective loading and configuration analysis to complete Connector initialization and subsequent operation. Source Connector implements the poll method, and Sink Connector implements The put method uniformly uses `ConnectorRecord` to carry data. Both Source Connector and Sink Connector can operate independently.

<a id="design-document-connect-connectors--connectorrecord-with-cloudevents"></a>

#### ConnectorRecord with CloudEvents

`ConnectorRecord` is a connector layer data protocol. When workers interact with EventMesh, a protocol adapter needs to be developed to convert `ConnectorRecord` to CloudEvents protocol.

<a id="design-document-connect-connectors--registry"></a>

#### Registry

The Registry module is responsible for storing the synchronization progress of synchronizing data of different Connector instances, ensuring high availability between multiple Connector images or instances.

- [Connector](#design-document-connect-connectors--connector)
- [Source](#design-document-connect-connectors--source)
- [Sink](#design-document-connect-connectors--sink)
- [CloudEvents](#design-document-connect-connectors--cloudevents)
- [Implements](#design-document-connect-connectors--implements)
- [Technical Solution](#design-document-connect-connectors--technical-solution)
  - [Structure and process](#design-document-connect-connectors--structure-and-process)
  - [Design Detail](#design-document-connect-connectors--design-detail)
  - [Description](#design-document-connect-connectors--description)

---

<a id="design-document-connect-rabbitmq-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/rabbitmq-connector/ -->

<!-- page_index: 22 -->

# RabbitMQ

Version: v1.12.0

# RabbitMQ

<a id="design-document-connect-rabbitmq-connector--rabbitmqsinkconnector-from-eventmesh-to-rabbitmq"></a>

## RabbitMQSinkConnector: From EventMesh to RabbitMQ

1. launch your RabbitMQ server and EventMesh Runtime.
2. enable sinkConnector and check `sink-config.yml`.
3. start your `RabbitMQConnectorServer`, it will subscribe to the topic defined in `pubSubConfig.subject` of EventMesh Runtime and send data to `connectorConfig.queueName` in your RabbitMQ.
4. send a message to EventMesh with the topic defined in `pubSubConfig.subject` and then you will receive the message in RabbitMQ.

```yaml
pubSubConfig:
  # default port 10000
  meshAddress: your.eventmesh.server:10000
  subject: TopicTest
  idc: FT
  env: PRD
  group: rabbitmqSink
  appId: 5031
  userName: rabbitmqSinkUser
  passWord: rabbitmqPassWord
connectorConfig:
  connectorName: rabbitmqSink
  host: your.rabbitmq.server
  port: 5672
  username: coyrqpyz
  passwd: passwd
  virtualHost: coyrqpyz
  exchangeType: TOPIC
  # build-in exchangeName or name a new one after you create it in rabbitmq server.
  exchangeName: amq.topic
  # rabbitmq server will create the routingKey and queueName automatically after you connect to it if they aren't exist before.
  routingKey: eventmesh
  queueName: eventmesh
  autoAck: true
```

<a id="design-document-connect-rabbitmq-connector--rabbitmqsourceconnector-from-rabbitmq-to-eventmesh"></a>

## RabbitMQSourceConnector: From RabbitMQ to EventMesh

1. launch your RabbitMQ server and EventMesh Runtime.
2. enable sourceConnector and check `source-config.yml` (Basically the same as `sink-config.yml`)
3. start your `RabbitMQConnectorServer`, it will subscribe to the queue defined in `connectorConfig.queueName` in your RabbitMQ and send data to `pubSubConfig.subject` of EventMesh Runtime.
4. send a CloudEvent message to the queue and then you will receive the message in EventMesh.

- [RabbitMQSinkConnector: From EventMesh to RabbitMQ](#design-document-connect-rabbitmq-connector--rabbitmqsinkconnector-from-eventmesh-to-rabbitmq)
- [RabbitMQSourceConnector: From RabbitMQ to EventMesh](#design-document-connect-rabbitmq-connector--rabbitmqsourceconnector-from-rabbitmq-to-eventmesh)

---

<a id="design-document-connect-http-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/http-connector/ -->

<!-- page_index: 23 -->

# HTTP

Version: v1.12.0

# HTTP

<a id="design-document-connect-http-connector--http-source-connector"></a>

## HTTP Source Connector

<a id="design-document-connect-http-connector--configuration"></a>

### Configuration

Before using HTTP source connector, you need to configure the server.

- Please configure `sourceEnable` to `true` in `/resource/server-config.yml` to enable source functionality.
- Please configure the source connector in `/resource/source-config.yml`, only the configuration under `connectorConfig` is described here:
  - `connectorName`, name of the connector.
  - (required) `path`, path of the API.
  - (required) `port`, port of the API.
  - `idleTimeout`, idle TCP connection timeout in seconds. A connection will timeout and be closed if no data is received nor sent within the `idleTimeout` seconds. The default is 0, which means don't timeout.

<a id="design-document-connect-http-connector--startup"></a>

### Startup

1. start EventMesh Runtime
2. start eventmesh-connector-http

When finished, the HTTP source connector will act as an HTTP server.

<a id="design-document-connect-http-connector--sending-messages"></a>

### Sending messages

You can send messages to the source connector via HTTP.

```yaml
connectorConfig:
    connectorName: httpSource
    path: /test
    port: 3755
    idleTimeout: 5
```

The above example configures a URL `http://localhost:3755/test` in `source-config.yml`.

You can send messages in `binary` mode or `structured` mode as specified in [cloudevent-spec](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md).

Here are two examples:

1. Sending a message in `binary` mode.

```shell
curl --location --request POST 'http://localhost:3755/test' \
--header 'ce-id: 1' \
--header 'ce-specversion: 1.0' \
--header 'ce-type: com.example.someevent' \
--header 'ce-source: /mycontext' \
--header 'ce-subject: test_topic' \
--header 'Content-Type: text/plain' \
--data-raw 'testdata'
```

2. Sending a message in `structured` mode.

```shell
curl --location --request POST 'http://localhost:3755/test' \
--header 'Content-Type: application/cloudevents+json' \
--data-raw '{
    "id": "1",
    "specversion": "1.0",
    "type": "com.example.someevent",
    "source": "/mycontext",
    "subject":"test_topic",
    "datacontenttype":"text/plain",
    "data": "testdata"
}'
```

- [HTTP Source Connector](#design-document-connect-http-connector--http-source-connector)
  - [Configuration](#design-document-connect-http-connector--configuration)
  - [Startup](#design-document-connect-http-connector--startup)
  - [Sending messages](#design-document-connect-http-connector--sending-messages)

---

<a id="design-document-connect-redis-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/redis-connector/ -->

<!-- page_index: 24 -->

# Redis

Version: v1.12.0

# Redis

<a id="design-document-connect-redis-connector--redissinkconnector-from-eventmesh-to-redis-topic-queue"></a>

## RedisSinkConnector: From EventMesh to Redis topic queue

1. start your Redis instance if needed and EventMesh Runtime.
2. enable sinkConnector and check `sink-config.yml`.
3. start your `RedisConnectServer`, it will subscribe to the topic defined in `pubSubConfig.subject` of EventMesh Runtime and send data to `connectorConfig.topic` in your Redis.
4. send a message to EventMesh with the topic defined in `pubSubConfig.subject` and then you will receive the message in Redis.

```yaml
pubSubConfig:
  # default port 10000
  meshAddress: your.eventmesh.server:10000
  subject: TopicTest
  idc: FT
  env: PRD
  group: redisSink
  appId: 5031
  userName: redisSinkUser
  passWord: redisPassWord
connectorConfig:
  connectorName: redisSink
  server: redis://127.0.0.1:6379
  # the topic in redis
  topic: SinkTopic
```

<a id="design-document-connect-redis-connector--redissourceconnector-from-redis-topic-queue-to-eventmesh"></a>

## RedisSourceConnector: From Redis topic queue to EventMesh

1. start your Redis instance if needed and EventMesh Runtime.
2. enable sourceConnector and check `source-config.yml` (Basically the same as `sink-config.yml`)
3. start your `RedisConnectServer`, it will subscribe to the topic defined in `connectorConfig.topic` in your Redis and send data to `pubSubConfig.subject` of EventMesh Runtime.
4. send a CloudEvent message to the topic in Redis, and you will receive the message in EventMesh.

- [RedisSinkConnector: From EventMesh to Redis topic queue](#design-document-connect-redis-connector--redissinkconnector-from-eventmesh-to-redis-topic-queue)
- [RedisSourceConnector: From Redis topic queue to EventMesh](#design-document-connect-redis-connector--redissourceconnector-from-redis-topic-queue-to-eventmesh)

---

<a id="design-document-connect-mongodb-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/mongodb-connector/ -->

<!-- page_index: 25 -->

# MongoDB

Version: v1.12.0

# MongoDB

<a id="design-document-connect-mongodb-connector--mongodbsinkconnector-from-eventmesh-to-mongodb"></a>

## MongoDBSinkConnector: From EventMesh to MongoDB

1. launch your MongoDB server and EventMesh Runtime.
2. enable sinkConnector and check `sink-config.yml`.
3. start your MongoDBConnectorServer, it will subscribe to the topic defined in `pubSubConfig.subject` of EventMesh Runtime and send data to `connectorConfig.collection` in your MongoDB.
4. send a message to EventMesh with the topic defined in `pubSubConfig.subject` and then you will receive the message in MongoDB.

```yaml
pubSubConfig:
  # default port 10000
  meshAddress: your.eventmesh.server:10000
  subject: TopicTest
  idc: FT
  env: PRD
  group: mongodbSink
  appId: 5031
  userName: mongodbSinkUser
  passWord: mongodbPassWord
connectorConfig:
  connectorName: mongodbSink
  # REPLICA_SET or STANDALONE is supported
  connectorType: STANDALONE
  # mongodb://root:root@127.0.0.1:27018,127.0.0.1:27019
  url: mongodb://127.0.0.1:27018
  database: yourDB
  collection: yourCol
```

<a id="design-document-connect-mongodb-connector--mongodbsourceconnector-from-mongodb-to-eventmesh"></a>

## MongoDBSourceConnector: From MongoDB to EventMesh

1. launch your MongoDB server and EventMesh Runtime.
2. enable sourceConnector and check `source-config.yml` (Basically the same as `sink-config.yml`)
3. start your `MongoDBSourceConnector`, it will subscribe to the collection defined in `connectorConfig.collection` in your MongoDB and send data to `pubSubConfig.subject` of EventMesh Runtime.
4. write a CloudEvent message to `yourCol` at `yourDB` in your MongoDB and then you will receive the message in EventMesh.

- [MongoDBSinkConnector: From EventMesh to MongoDB](#design-document-connect-mongodb-connector--mongodbsinkconnector-from-eventmesh-to-mongodb)
- [MongoDBSourceConnector: From MongoDB to EventMesh](#design-document-connect-mongodb-connector--mongodbsourceconnector-from-mongodb-to-eventmesh)

---

<a id="design-document-connect-knative-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/knative-connector/ -->

<!-- page_index: 26 -->

# Knative

Version: v1.12.0

# Knative

> With the changes in the design of the Knative connector, this document is currently temporarily outdated.

<a id="design-document-connect-knative-connector--prerequisite"></a>

## Prerequisite

<a id="design-document-connect-knative-connector--create-knative-source-and-sink"></a>

### Create Knative Source and Sink

We use the *cloudevents-player* [Knative service](https://knative.dev/docs/serving/) as an example. If you do not know how to create *cloudevents-player* Knative service as source and sink, please follow the steps in this [link](https://knative.dev/docs/getting-started/first-source/#creating-your-first-source).

<a id="design-document-connect-knative-connector--set-up-eventmesh-configuration"></a>

### Set up EventMesh Configuration

- Add the following lines to [eventmesh-starter/build.gradle](https://github.com/apache/eventmesh/blob/master/eventmesh-starter/build.gradle) file.

```text
plugins {
    id 'application'
}

application {
    mainClass = project.hasProperty("mainClass") ? project.getProperty("mainClass") : 'org.apache.eventmesh.starter.StartUp'
    applicationDefaultJvmArgs = [
            '-Dlog4j.configurationFile=../eventmesh-runtime/conf/log4j2.xml', '-Deventmesh.log.home=../eventmesh-runtime/logs', '-Deventmesh.home=../eventmesh-runtime', '-DconfPath=../eventmesh-runtime/conf'
    ]
}

dependencies {
    implementation project(":eventmesh-connector-plugin:eventmesh-connector-knative")
    implementation project(":eventmesh-runtime")
}
```

- Add the following lines to [eventmesh-examples/build.gradle](https://github.com/apache/eventmesh/blob/master/eventmesh-examples/build.gradle) file.

```text
plugins {
    id 'application'
}

application {
    mainClass = project.hasProperty("mainClass") ? project.getProperty("mainClass") : 'NULL'
}
```

- Set `eventMesh.connector.plugin.type=knative` in [eventmesh-runtime/conf/eventmesh.properties](https://github.com/apache/eventmesh/blob/master/eventmesh-runtime/conf/eventmesh.properties) file.

<a id="design-document-connect-knative-connector--demo"></a>

## Demo

<a id="design-document-connect-knative-connector--publish-an-event-message-from-knative-and-subscribe-from-eventmesh"></a>

### Publish an Event Message from Knative and Subscribe from EventMesh

<a id="design-document-connect-knative-connector--step-1-start-an-eventmesh-runtime-server"></a>

#### Step 1: Start an EventMesh Runtime Server

```bash
$ cd eventmesh-starter
$ ../gradlew -PmainClass=org.apache.eventmesh.starter.StartUp run
```

<a id="design-document-connect-knative-connector--step-2-publish-an-event-message-from-knative"></a>

#### Step 2: Publish an Event Message from Knative

```bash
$ curl -i http://cloudevents-player.default.127.0.0.1.sslip.io -H "Content-Type: application/json" -H "Ce-Id: 123456789" -H "Ce-Specversion: 1.0" -H "Ce-Type: some-type" -H "Ce-Source: command-line" -d '{"msg":"Hello CloudEvents!"}'
```

<a id="design-document-connect-knative-connector--step-3-subscribe-from-an-eventmesh"></a>

#### Step 3: Subscribe from an EventMesh

- Set `public static final String EVENTMESH_HTTP_ASYNC_TEST_TOPIC = "messages";` in [ExampleConstants.java](https://github.com/apache/eventmesh/blob/master/eventmesh-examples/src/main/java/org/apache/eventmesh/common/ExampleConstants.java) file.

```bash
$ cd eventmesh-examples
$ ../gradlew -PmainClass=org.apache.eventmesh.http.demo.sub.SpringBootDemoApplication run
```

<a id="design-document-connect-knative-connector--expected-result"></a>

#### Expected Result

The following message with `data` field as `Hello CloudEvents!` will be printed on the console of EventMesh server.

```bash
2022-09-05 16:37:58,237 INFO  [eventMesh-clientManage-] DefaultConsumer(DefaultConsumer.java:60) - \
[{"event":{"attributes":{"datacontenttype":"application/json","id":"123456789","mediaType":"application/json",\
"source":"command-line","specversion":"1.0","type":"some-type"},"data":{"msg":"Hello CloudEvents!"},"extensions":{}},\
"id":"123456789","receivedAt":"2022-09-05T10:37:49.537658+02:00[Europe/Madrid]","type":"RECEIVED"}]
```

<a id="design-document-connect-knative-connector--publish-an-event-message-from-eventmesh-and-subscribe-from-knative"></a>

### Publish an Event Message from EventMesh and Subscribe from Knative

<a id="design-document-connect-knative-connector--step-1-start-an-eventmesh-runtime-server-1"></a>

#### Step 1: Start an EventMesh Runtime Server

```bash
$ cd eventmesh-starter
$ ../gradlew -PmainClass=org.apache.eventmesh.starter.StartUp run
```

<a id="design-document-connect-knative-connector--step-2-publish-an-event-message-from-eventmesh"></a>

#### Step 2: Publish an Event Message from EventMesh

We use a test program to demo this function.

```bash
$ cd eventmesh-connector-plugin/eventmesh-connector-knative
$ ../../gradlew clean test --tests KnativeProducerImplTest.testPublish
```

<a id="design-document-connect-knative-connector--step-3-subscribe-from-knative"></a>

#### Step 3: Subscribe from Knative

```bash
$ curl http://cloudevents-player.default.127.0.0.1.sslip.io/messages
```

<a id="design-document-connect-knative-connector--expected-result-1"></a>

#### Expected Result

The following message with `data` field as `Hello Knative from EventMesh!` will be printed on the console of EventMesh server.

```bash
2022-09-05 16:52:41,633 INFO  [eventMesh-clientManage-] DefaultConsumer(DefaultConsumer.java:60) - \
[{"event":{"attributes":{"datacontenttype":"application/json","id":"1234","mediaType":"application/json",\
"source":"java-client","specversion":"1.0","type":"some-type"},"data":{"msg":["Hello Knative from EventMesh!"]},"extensions":{}},"id":"1234","receivedAt":"2022-09-05T10:52:32.999273+02:00[Europe/Madrid]","type":"RECEIVED"}]
```

- [Prerequisite](#design-document-connect-knative-connector--prerequisite)
  - [Create Knative Source and Sink](#design-document-connect-knative-connector--create-knative-source-and-sink)
  - [Set up EventMesh Configuration](#design-document-connect-knative-connector--set-up-eventmesh-configuration)
- [Demo](#design-document-connect-knative-connector--demo)
  - [Publish an Event Message from Knative and Subscribe from EventMesh](#design-document-connect-knative-connector--publish-an-event-message-from-knative-and-subscribe-from-eventmesh)
  - [Publish an Event Message from EventMesh and Subscribe from Knative](#design-document-connect-knative-connector--publish-an-event-message-from-eventmesh-and-subscribe-from-knative)

---

<a id="design-document-connect-lark-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/lark-connector/ -->

<!-- page_index: 27 -->

# Feishu/Lark

Version: v1.12.0

# Feishu/Lark

<a id="design-document-connect-lark-connector--lark-sink-server-config-and-start"></a>

## Lark Sink Server Config And Start

Before using eventmesh-connector-lark to sink events, you need to configure the server.

- Please customize `sinkEnable`=`true`/`false` in `/resource/server-config.yml` to turn on/off the sink function.
- Regarding `/resource/sink-config.yml`, only the configuration under `sinkConnectorConfig` is explained here:
  - `connectorName`, specify the connector name
  - (required) `appId`, the appId obtained from lark
  - (required) `appSecret`, the appSecret obtained from lark
  - `receiveIdType`, the type of receiving Id, the default and recommended use is `open_id`. Optional open\_id/user\_id/union\_id/email/chat\_id.
  - (Required) `receiveId`, receive Id, needs to correspond to `receiveIdType`.
  - `sinkAsync`, whether to asynchronously sink events
  - `maxRetryTimes`, the maximum number of retransmissions when the sink event fails. The default is 3 times.
  - `retryDelayInMills`, when the sink event fails, the time interval for retransmitting the event. Default is 1s, unit is milliseconds.

<a id="design-document-connect-lark-connector--sink-cloudevent-to-lark"></a>

## Sink CloudEvent To Lark

When using the eventmesh-connector-lark sinking event, you need to add the corresponding extension filed in CloudEvent:

- When key=`templatetype4lark`, value=`text`/`markdown`, indicating the text type of the event.
- When text type is markdown, you can add extension: key=`markdownmessagetitle4lark`, value indicates the title of the event.
- When key=`atusers4lark`, value=`id-0,name-0;id-1,name-1`, indicating that the event requires `@`certain users.
  - It is recommended to use **open\_id** for id.
  - When the text is of text type, the id can be **open\_id/union\_id/user\_id**; when the text is of markdown type, the id can be **open\_id/user\_id**. In particular, when the application type is [custom robot](https://open.larksuite.com/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN) and the text is of markdown type, only the use of **open\_id** to `@` the user is supported.
  - When the text is of text type and the id is invalid, name will be used instead for display; when the text is of markdown type and the id is invalid, an exception will be thrown directly (you should try to ensure the correctness of the id, and name can be considered omitted).
- When key=`atall4lark`, value=`true`/`false`, indicating that the event requires `@` everyone.

<a id="design-document-connect-lark-connector--lark-open-platform-api"></a>

## Lark Open Platform API

For the Lark open platform API involved in this module, please click the following link:

- **Send Message**, please [view here](https://open.larksuite.com/document/server-docs/im-v1/message/create?appId=cli_a5e1bc31507ed00c)
- **text**, please [view here](https://open.larksuite.com/document/server-docs/im-v1/message-content-description/create_json#c9e08671)
- **markdown**, please [view here](https://open.larksuite.com/document/common-capabilities/message-card/message-cards-content/using-markdown-tags)

- [Lark Sink Server Config And Start](#design-document-connect-lark-connector--lark-sink-server-config-and-start)
- [Sink CloudEvent To Lark](#design-document-connect-lark-connector--sink-cloudevent-to-lark)
- [Lark Open Platform API](#design-document-connect-lark-connector--lark-open-platform-api)

---

<a id="design-document-connect-dingtalk-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/dingtalk-connector/ -->

<!-- page_index: 28 -->

# DingTalk

Version: v1.12.0

# DingTalk

<a id="design-document-connect-dingtalk-connector--dingtalksinkconnector-from-eventmesh-to-dingtalk"></a>

## DingtalkSinkConnector: From EventMesh to DingTalk

1. launch your EventMesh Runtime.
2. enable sinkConnector and check `sink-config.yml`.
3. send a message to EventMesh with the topic defined in `pubSubConfig.subject`

```yaml
pubSubConfig:
  # default port 10000
  meshAddress: your.eventmesh.server:10000
  subject: TEST-TOPIC-DINGTALK
  idc: FT
  env: PRD
  group: dingTalkSink
  appId: 5034
  userName: dingTalkSinkUser
  passWord: dingTalkPassWord
sinkConnectorConfig:
  connectorName: dingTalkSink
  # Please refer to: https://open.dingtalk.com/document/orgapp/the-robot-sends-a-group-message
  appKey: dingTalkAppKey
  appSecret: dingTalkAppSecret
  openConversationId: dingTalkOpenConversationId
  robotCode: dingTalkRobotCode
```

<a id="design-document-connect-dingtalk-connector--cloudevent-attributes"></a>

### CloudEvent Attributes

When using the eventmesh-connector-dingtalk sinking event, you need to add the corresponding extension filed in CloudEvent:

- When key=`dingtalktemplatetype`, value=`text`/`markdown`, indicating the text type of the event.
- When text type is markdown, you can add extension: key=`dingtalkmarkdownmessagetitle`, value indicates the title of the event.

- [DingtalkSinkConnector: From EventMesh to DingTalk](#design-document-connect-dingtalk-connector--dingtalksinkconnector-from-eventmesh-to-dingtalk)
  - [CloudEvent Attributes](#design-document-connect-dingtalk-connector--cloudevent-attributes)

---

<a id="design-document-connect-wecom-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/wecom-connector/ -->

<!-- page_index: 29 -->

# WeCom

Version: v1.12.0

# WeCom

<a id="design-document-connect-wecom-connector--wecomsinkconnector-from-eventmesh-to-wecom"></a>

## WecomSinkConnector: From EventMesh to WeCom

1. launch your EventMesh Runtime.
2. enable sinkConnector and check `sink-config.yml`.
3. send a message to EventMesh with the topic defined in `pubSubConfig.subject`

```yaml
pubSubConfig:
  # default port 10000
  meshAddress: your.eventmesh.server:10000
  subject: TEST-TOPIC-WECOM
  idc: FT
  env: PRD
  group: weComSink
  appId: 5034
  userName: weComSinkUser
  passWord: weComPassWord
sinkConnectorConfig:
  connectorName: weComSink
  # Please refer to: https://developer.work.weixin.qq.com/document/path/90236
  robotWebhookKey: weComRobotWebhookKey
```

<a id="design-document-connect-wecom-connector--cloudevent-attributes"></a>

### CloudEvent Attributes

When using the eventmesh-connector-wecom sinking event, you need to add the corresponding extension filed in CloudEvent:

- When key=`wecomtemplatetype`, value=`text`/`markdown`, indicating the text type of the event.

- [WecomSinkConnector: From EventMesh to WeCom](#design-document-connect-wecom-connector--wecomsinkconnector-from-eventmesh-to-wecom)
  - [CloudEvent Attributes](#design-document-connect-wecom-connector--cloudevent-attributes)

---

<a id="design-document-connect-slack-connector"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/connect/slack-connector/ -->

<!-- page_index: 30 -->

# Slack

Version: v1.12.0

# Slack

<a id="design-document-connect-slack-connector--slacksinkconnector-from-eventmesh-to-slack"></a>

## SlackSinkConnector: From EventMesh to Slack

1. launch your EventMesh Runtime.
2. enable sinkConnector and check `sink-config.yml`.
3. send a message to EventMesh with the topic defined in `pubSubConfig.subject`

```yaml
pubSubConfig:
  # default port 10000
  meshAddress: your.eventmesh.server:10000
  subject: TEST-TOPIC-SLACK
  idc: FT
  env: PRD
  group: slackSink
  appId: 5034
  userName: slackSinkUser
  passWord: slackPassWord
sinkConnectorConfig:
  connectorName: slackSink
  # Please refer to: https://api.slack.com/messaging/sending
  appToken: slackAppToken
  channelId: slackChannelId
```

- [SlackSinkConnector: From EventMesh to Slack](#design-document-connect-slack-connector--slacksinkconnector-from-eventmesh-to-slack)

---

<a id="design-document-schema-registry"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/schema-registry/ -->

<!-- page_index: 31 -->

# EventMesh Schema Registry (OpenSchema)

Version: v1.12.0

# EventMesh Schema Registry (OpenSchema)

<a id="design-document-schema-registry--overview-of-schema-and-schema-registry"></a>

## Overview of Schema and Schema Registry

<a id="design-document-schema-registry--schema"></a>

### Schema

A Schema stands for the description of serialization instances(string/stream/file/...) and has two properties. First, it is also in the format of serialization type. Second, it defines what requirements such serialized instances should satisfy.

Besides describing a serialization instance, a Schema may also be used for validating whether an instance is legitimate. The reason is that it defines the `type`(and other properties) of a serialized instance and inside keys. Taking JSON Schema for example, it could not only be referred when describing a JSON string, but also be used for validating whether a string satisfies properties defined in the schema[[1]](#design-document-schema-registry--references).

Commonly, there are JSON Schema, Protobuf Schema, and Avro Schema.

<a id="design-document-schema-registry--schema-registry"></a>

### Schema Registry

Schema Registry is a server provides RESTful interfaces. It could receive and store Schemas from clients, as well as provide intrefaces for other clients to retrieve Schemas from it.

It could be applied to validation process and (de-)serialization process.

<a id="design-document-schema-registry--comparison-of-schema-registry-in-different-projects"></a>

### Comparison of Schema Registry in Different Projects

<table><thead><tr><th align="center">Project</th><th align="left">Application</th></tr></thead><tbody><tr><td align="center">EMQ<a href="#design-document-schema-registry--references">[2]</a></td><td align="left">Mainly in (de-)serialization process. Use "Schema Registry" and "Rule Matching" to transfer a message from one serialization format to another.</td></tr><tr><td align="center">Pulsar<a href="#design-document-schema-registry--references">[3]</a></td><td align="left">Mainly in validation process. Use "Schema Registry" to validate a message.</td></tr><tr><td align="center">Confluentinc<a href="#design-document-schema-registry--references">[4]</a></td><td align="left">In both validation and (de-)serialization process.</td></tr></tbody></table>
<a id="design-document-schema-registry--overview-of-openschema"></a>

## Overview of OpenSchema

OpenSchema[[5]](#design-document-schema-registry--references) proposes a specification for data schema when exchanging the message and event in more and more modern cloud-native applications. It designs a RESTful interface for storing and retrieving such as Avro, JSON Schema, and Protobuf3 schemas from three aspects(subject/schema/compatibility).

<a id="design-document-schema-registry--requirementsgoals"></a>

## Requirements(Goals)

<table><thead><tr><th align="left">Requirement ID</th><th>Requirement Description</th><th>Comments</th></tr></thead><tbody><tr><td align="left">F-1</td><td>In transmission, no message needs to contain schema information which bring efficiency.</td><td>Functionality</td></tr><tr><td align="left">F-2</td><td>The message content from producer could be validated whether serialized correctly according to schema.</td><td>Functionality</td></tr></tbody></table>
<a id="design-document-schema-registry--design-details"></a>

## Design Details

<a id="design-document-schema-registry--architecture"></a>

### Architecture

![OpenSchema](assets/images/schema-registry-architecture-e376404fc6051685e1e14f6ea15e9bd8_ae3383bb48f215d2.png)

<a id="design-document-schema-registry--process-of-transferring-messages-under-schema-registry"></a>

### Process of Transferring Messages under Schema Registry

![Process](assets/images/schema-registry-process-204fb6690bbd4f93f6b3571df13b114b_1ee631198daea22b.jpg)

The highlevel process of messages transmission contains 10 steps as follows:

- 1: Consumer subscribes "TOPIC" messages from EventMesh.
- 2: Producer registers a schema to EventMesh.
- 3: EventMesh registers a schema to Schema Registry.
- 4: Schema Registry returns the id of newly created schema; EventMesh caches such id and schema.
- 5: EventMesh returns the id of schema to Producer.
- 6: Producer patches the id in front of messages and send messages to EventMesh.
- 7: EventMesh validates the messages in the entry port and send it to EventStore; EventMesh retrieves messages from EventStore.
- 8: EventMesh unpatches the id and send it to Schema Registry(if such `<id, schema>` does not exists in local cache).
- 9: Schema Registry returns schema and EventMesh caches it.
- 10: EventMesh patches schema in front of messages and push it to consumer.

<a id="design-document-schema-registry--current-progress"></a>

## Current Progress

<a id="design-document-schema-registry--status"></a>

### Status

**Current state**: Developing

**Discussion thread**: ISSUE #339

<a id="design-document-schema-registry--proposed-changes"></a>

### Proposed Changes

The proposal has two aspects.

First is a separated Open Schema Registry, which includes storage and compatibility check for schema.
This proposal is under developing.

Second is the integration of Open Schema in EventMesh, which includes validation for schema. This proposal is to be developed.

As for the first proposal, some developing statuses are as follows.

<a id="design-document-schema-registry--status-code-and-exception-code"></a>

#### Status Code and Exception Code

<table><thead><tr><th>No.</th><th align="center">Status Code</th><th align="center">Exception Code</th><th align="center">Description</th><th align="center">status</th></tr></thead><tbody><tr><td>1</td><td align="center">401</td><td align="center">40101</td><td align="center">Unauthorized Exception</td><td align="center">✔</td></tr><tr><td>2</td><td align="center">404</td><td align="center">40401</td><td align="center">Schema Non- Exception</td><td align="center">✔</td></tr><tr><td>3</td><td align="center">^</td><td align="center">40402</td><td align="center">Subject Non-exist Exception</td><td align="center">✔</td></tr><tr><td>4</td><td align="center">^</td><td align="center">40403</td><td align="center">Version Non-exist Exception</td><td align="center">✔</td></tr><tr><td>5</td><td align="center">409</td><td align="center">40901</td><td align="center">Compatibility Exception</td><td align="center">✔</td></tr><tr><td>6</td><td align="center">422</td><td align="center">42201</td><td align="center">Schema Format Exception</td><td align="center">✔</td></tr><tr><td>7</td><td align="center">^</td><td align="center">42202</td><td align="center">Subject Format Exception</td><td align="center">✔</td></tr><tr><td>8</td><td align="center">^</td><td align="center">42203</td><td align="center">Version Format Exception</td><td align="center">✔</td></tr><tr><td>9</td><td align="center">^</td><td align="center">42204</td><td align="center">Compatibility Format Exception</td><td align="center">✔</td></tr><tr><td>10</td><td align="center">500</td><td align="center">50001</td><td align="center">Storage Service Exception</td><td align="center">✔</td></tr><tr><td>11</td><td align="center">^</td><td align="center">50002</td><td align="center">Timeout Exception</td><td align="center">✔</td></tr></tbody></table>
<a id="design-document-schema-registry--api-development-status"></a>

#### API Development Status

<table><thead><tr><th>No.</th><th>Type</th><th>URL</th><th>response</th><th>exception</th><th>code</th><th>test</th></tr></thead><tbody><tr><td>1</td><td>GET</td><td>/schemas/ids/{string: id}</td><td><code>Schema.class</code></td><td>40101\40401\50001</td><td>✔</td><td>❌</td></tr><tr><td>2</td><td>GET</td><td>/schemas/ids/{string: id}/subjects</td><td><code>SubjectAndVersion.class</code></td><td>40101\40401\50001</td><td>✔</td><td>❌</td></tr><tr><td>3</td><td>GET</td><td>/subjects</td><td><code>List\&lt;String&gt;</code></td><td>40101\50001</td><td>✔</td><td>❌</td></tr><tr><td>4</td><td>GET</td><td>/subjects/{string: subject}/versions</td><td><code>List\&lt;Integer&gt;</code></td><td>40101\40402\50001</td><td>✔</td><td>❌</td></tr><tr><td>5</td><td>DELETE</td><td>/subjects/(string: subject)</td><td><code>List\&lt;Integer&gt;</code></td><td>40101\40402\50001</td><td>✔</td><td>❌</td></tr><tr><td>6</td><td>GET</td><td>/subjects/(string: subject)</td><td><code>Subject.class</code></td><td>40101\40402\50001</td><td>✔</td><td>❌</td></tr><tr><td>7</td><td>GET</td><td>/subjects/(string: subject)/versions/(version: version)/schema</td><td><code>SubjectWithSchema.class</code></td><td>40101\40402\40403\50001</td><td>✔</td><td>❌</td></tr><tr><td>8</td><td>POST</td><td>/subjects/(string: subject)/versions</td><td><code>SchemaIdResponse.class</code></td><td>40101\40901\42201\50001\50002</td><td>-</td><td>❌</td></tr><tr><td>9</td><td>POST</td><td>/subjects/(string: subject)/</td><td><code>Subject.class</code></td><td>40101\40901\42202\50001\50002</td><td>✔</td><td>❌</td></tr><tr><td>10</td><td>DELETE</td><td>/subjects/(string: subject)/versions/(version: version)</td><td><code>int</code></td><td>40101\40402\40403\40901\50001</td><td>-</td><td>❌</td></tr><tr><td>11</td><td>POST</td><td>/compatibility/subjects/(string: subject)/versions/(version: version)</td><td><code>CompatibilityResultResponse.class</code></td><td>40101\40402\40403\42201\42203\50001</td><td>-</td><td>❌</td></tr><tr><td>12</td><td>GET</td><td>/compatibility/(string: subject)</td><td><code>Compatibility.class</code></td><td>40101\40402\50001</td><td>✔</td><td>❌</td></tr><tr><td>13</td><td>PUT</td><td>/compatibility/(string: subject)</td><td><code>Compatibility.class</code></td><td>40101\40402\40901\42204\50001</td><td>-</td><td>❌</td></tr></tbody></table>
<a id="design-document-schema-registry--overall-project-structure"></a>

#### Overall Project Structure

`SchemaController.java`+`SchemaService.java` : `OpenSchema 7.1.1~7.1.2 (API 1~2)`

`SubjectController.java`+`SubjectService.java` : `OpenSchema 7.2.1~7.2.8 (API 3~10)`

`CompatibilityController.java`+`CompatibilityService.java` : `OpenSchema 7.3.1~7.3.3 (API 11~13)` + `Check for Compatibility`

![Project Structure](assets/images/schema-registry-project-structure-468c4e4f7a31528a51d8d289fb4afb50_725be7118fd3a88c.png)

<a id="design-document-schema-registry--references"></a>

## References

[1][schema validator (github.com)](<https://github.com/search?q=schema+validator>)

[2][EMQ: Schema Registry](<https://www.jianshu.com/p/33e0655c642b>)

[3][Pulsar: Schema Registry](<https://mp.weixin.qq.com/s/PaB66-Si00cX80py5ig5Mw>)

[4][confluentinc/schema-registry](<https://github.com/confluentinc/schema-registry>)

[5][openmessaging/openschema](<https://github.com/openmessaging/openschema>)

- [Overview of Schema and Schema Registry](#design-document-schema-registry--overview-of-schema-and-schema-registry)
  - [Schema](#design-document-schema-registry--schema)
  - [Schema Registry](#design-document-schema-registry--schema-registry)
  - [Comparison of Schema Registry in Different Projects](#design-document-schema-registry--comparison-of-schema-registry-in-different-projects)
- [Overview of OpenSchema](#design-document-schema-registry--overview-of-openschema)
- [Requirements(Goals)](#design-document-schema-registry--requirementsgoals)
- [Design Details](#design-document-schema-registry--design-details)
  - [Architecture](#design-document-schema-registry--architecture)
  - [Process of Transferring Messages under Schema Registry](#design-document-schema-registry--process-of-transferring-messages-under-schema-registry)
- [Current Progress](#design-document-schema-registry--current-progress)
  - [Status](#design-document-schema-registry--status)
  - [Proposed Changes](#design-document-schema-registry--proposed-changes)
- [References](#design-document-schema-registry--references)

---

<a id="design-document-spi"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/spi/ -->

<!-- page_index: 32 -->

# Service Provider Interface

Version: v1.12.0

# Service Provider Interface

<a id="design-document-spi--introduction"></a>

## Introduction

In order to improve scalability, EventMesh introduce the SPI (Service Provider Interface) mechanism, which can help to automatically find the concrete implementation
class of the extended interface at runtime and load it dynamically. In EventMesh, all extension modules are implemented by using plugin.
User can develop custom plugins by simply implementing extended interfaces, and select the plugin to be run at runtime by simply declare at configuration.

<a id="design-document-spi--eventmesh-spi-module"></a>

## eventmesh-spi module

The implementation of SPI is at eventmesh-spi module, there are three main classes `EventMeshSPI`, `EventMeshExtensionFactory` and `ExtensionClassLoader`.

<a id="design-document-spi--eventmeshspi"></a>

### EventMeshSPI

EventMeshSPI is an SPI declaration annotation, all extended interface that want to be implemented should be declared by @EventMeshSPI.

```java
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE})
public @interface EventMeshSPI {
    /**
     * If true, the spi instance is singleton
     */
    boolean isSingleton() default false;
}
```

Use annotation to declare the interface is an SPI extended interface can improve the readability of the code.
On the other hand, @EventMeshSPI contains a isSingleton attribute which used to declare whether the extension instance is a singleton.
If this attribute is true, that means the instance of this interface will be singleton.

<a id="design-document-spi--eventmeshextensionfactory"></a>

### EventMeshExtensionFactory

EventMeshExtensionFactory is a factory used to get the SPI extension instance which contains a static method `getExtension(Class<T> extensionType, String extensionName)`.

```java
public enum EventMeshExtensionFactory {
    /**
     * @param extensionType extension plugin class type
     * @param extensionName extension instance name
     * @param <T>           the type of the plugin
     * @return plugin instance
     */
    public static <T> T getExtension(Class<T> extensionType, String extensionName) {
        /* ... */
    }
}
```

If you want to get the extension instance, you should use EventMeshExtensionFactory.

<a id="design-document-spi--extensionclassloader"></a>

### ExtensionClassLoader

ExtensionClassLoader is used to load extension instance classed, it has two subclass MetaInfExtensionClassLoader and JarExtensionClassLoader.

```java
/**
 * Load extension class
 * <ul>
 *     <li>{@link MetaInfExtensionClassLoader}</li>
 *     <li>{@link JarExtensionClassLoader}</li>
 * </ul>
 */
public interface ExtensionClassLoader {
    /**
     * load
     *
     * @param extensionType extension type class
     * @param <T>           extension type
     * @return extension instance name to extension instance class
     */
    <T> Map<String, Class<?>> loadExtensionClass(Class<T> extensionType);
}
```

MetaInfExtensionClassLoader used to load class from classPath, and JarExtensionClassLoader used to load class from extension jar on the plugin directory.
In the future, we might support the implementation to load from the maven repository.

<a id="design-document-spi--spi-use-case"></a>

## SPI use case

The following is an example of how to use the SPI to declare a plugin.

First, we create an eventmesh-connector-api module, and define the extension interface MeshMQProducer, and we use @EventMeshSPI on the MeshMQProducer, which indicates the MeshMQProducer is an SPI interface.

```java
@EventMeshSPI(isSingleton = false)
public interface MeshMQProducer extends Producer {
    /* ... */
}
```

Then we create an eventmesh-connector-rocketmq module, which contains the concrete implementation named RocketMQProducerImpl.

```java
public class RocketMQProducerImpl implements MeshMQProducer {
    /* ... */
}
```

At the same time, we need to create a file with the full qualified name of the SPI interface under the resource/META-INF/eventmesh directory
in the eventmesh-connector-rocketmq module.

org.apache.eventmesh.api.producer.Producer

The content of the file is the extension instance name and the corresponding instance full class name

```properties
rocketmq=org.apache.eventmesh.connector.rocketmq.producer.RocketMQProducerImpl
```

At this point, an SPI expansion module is complete. We can use `EventMeshExtensionFactory.getExtension(MeshMQProducer.class, "rocketmq")` to get the `RocketMQProducerImpl` instance.

- [Introduction](#design-document-spi--introduction)
- [eventmesh-spi module](#design-document-spi--eventmesh-spi-module)
  - [EventMeshSPI](#design-document-spi--eventmeshspi)
  - [EventMeshExtensionFactory](#design-document-spi--eventmeshextensionfactory)
  - [ExtensionClassLoader](#design-document-spi--extensionclassloader)
- [SPI use case](#design-document-spi--spi-use-case)

---

<a id="design-document-stream"></a>

<!-- source_url: https://eventmesh.apache.org/docs/design-document/stream/ -->

<!-- page_index: 33 -->

# EventMesh Stream

Version: v1.12.0

# EventMesh Stream

<a id="design-document-stream--overview-of-event-streaming"></a>

## Overview of Event Streaming

Event Streaming is an implementation of Pub/Sub architecture pattern,it consist of

- Message or Event: Change of State.
- Topic: Partition in messaging middle ware broker.
- Consumer: Can subscribe to read events from broker topic.
- Producer: Generate events

Streaming of event is continuous flow of events in order to maintain order between events, events flow should be in a specific direction means from producers to consumers.

<a id="design-document-stream--requirements"></a>

## Requirements

<a id="design-document-stream--functional-requirements"></a>

### Functional Requirements

<table><thead><tr><th>Requirement ID</th><th>Requirement Description</th><th>Comments</th></tr></thead><tbody><tr><td>F-1</td><td>EventMesh users should be able to achieve Event Streaming functionality in EventMesh</td><td>Functionality</td></tr><tr><td>F-2</td><td>EventMesh users can apply dynamic user specific logics for routing, filter, transformation etc</td><td>Functionality</td></tr></tbody></table>
<a id="design-document-stream--design-details"></a>

## Design Details

We are introduce EventMesh Stream component allow us to use programming model and binder abstractions
from Spring Cloud Stream natively within Apache Camel.

[Spring-Cloud-Stream](https://spring.io/projects/spring-cloud-stream) Spring Cloud Stream is a framework for building
highly scalable event-driven microservices connected with shared messaging systems.

[Apache Camel](https://camel.apache.org/) Camel is an Open Source integration framework that empowers you to quickly
and easily integrate various systems consuming or producing data.

<a id="design-document-stream--architecture"></a>

## Architecture

![Stream Architecture](assets/images/stream-architecture-619e3498c1cc2a3afa0830ff8a112b8f_cb942ce4f8d9b57a.png)

<a id="design-document-stream--design"></a>

## Design

<a id="design-document-stream--eventmesh-stream-component"></a>

### EventMesh-Stream Component

- Event
- Event Channel
- Event EndPoint
- Event Pipes & Filters
- Event Routes
- Event Converter

<a id="design-document-stream--event"></a>

#### Event

> A event is the smallest unit for transmitting data in system. It structure divided into headers, body and attachments.

<a id="design-document-stream--event-channel"></a>

#### Event Channel

> A event channel is a logical channel in system, we are achieving by Spring Cloud Stream programming model, it has abstract functionality around messaging channels(As of now Spring `MessageChannel`).

<a id="design-document-stream--event-endpoint"></a>

#### Event EndPoint

> A event endpoint is the interface between an application and a messaging system. We can define two types of endpoint

- Consumer endpoint - Appears at start of a route and read incoming events from an incoming channel.
- Producer endpoint - Appears at end of a route and write incoming events to an outgoing channel.

<a id="design-document-stream--event-pipes-filters"></a>

#### Event Pipes & Filters

> We can construct a route by creating chain of filters( Apache Camel `Processor`), where the output of one filter is fed into input for next filter in the pipeline.
> The main advantage of the pipeline is that you can create complex event processing logic.

<a id="design-document-stream--event-routes"></a>

#### Event Routes

> A event router, is a type of filter on consumer and redirect them to the appropriate target endpoint based on a decision criteria.

<a id="design-document-stream--event-converter"></a>

#### Event Converter

> The event converter that modifies the contents of a event, translating it to a different format(i.e cloudevents -> Event (Camel) -> Binder Message(Spring Message) and vice versa).

<a id="design-document-stream--eventmesh-stream-component-interfaces"></a>

## EventMesh-Stream Component Interfaces

<a id="design-document-stream--component"></a>

### Component

Component interface is the primary entry point, you can use Component object as a factory to create EndPoint objects.

![Stream Component Interface](assets/images/stream-component-interface-ec9641e0807d88d099af905130cbbd1b_9631f6c1d523737f.png)

<a id="design-document-stream--endpoint"></a>

### EndPoint

EndPoint which is act as factories for creating Consumer, Producer and Event objects.

- `createConsumer()` — Creates a consumer endpoint, which represents the source endpoint at the beginning of a route.
- `createProducer()` — Creates a producer endpoint, which represents the target endpoint at the end of a route.

![Stream Component Routes](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlQAAABwCAYAAADYOu4gAAAGTHRFWHRteGZpbGUAJTNDbXhmaWxlJTIwaG9zdCUzRCUyMmFwcC5kaWFncmFtcy5uZXQlMjIlMjBtb2RpZmllZCUzRCUyMjIwMjEtMDctMjVUMTUlM0EzNCUzQTQ1LjI4NVolMjIlMjBhZ2VudCUzRCUyMjUuMCUyMChXaW5kb3dzJTIwTlQlMjAxMC4wJTNCJTIwV2luNjQlM0IlMjB4NjQpJTIwQXBwbGVXZWJLaXQlMkY1MzcuMzYlMjAoS0hUTUwlMkMlMjBsaWtlJTIwR2Vja28pJTIwQ2hyb21lJTJGOTEuMC40NDcyLjE2NCUyMFNhZmFyaSUyRjUzNy4zNiUyMiUyMGV0YWclM0QlMjJLTnZsbmNFLTZoU3RFZDAtcDZ6OCUyMiUyMHZlcnNpb24lM0QlMjIxNC45LjAlMjIlMjB0eXBlJTNEJTIyZGV2aWNlJTIyJTNFJTNDZGlhZ3JhbSUyMGlkJTNEJTIyejI5M3Y0dkRUYnQzc1VEbDFvQTglMjIlMjBuYW1lJTNEJTIyUGFnZS0xJTIyJTNFN1ZuYlV0c3dFUDJhUE1MWVZoTENJNFJRT3FVem1ZRXA5SWtSOWliV1ZMWXlzbkxqNjd1eTVhc1Nra0lhMHRDbmVJJTJGa3RmYWMxV1dWRnVsSGl5JTJCU1RzTHZJZ0RlOHB4ZzBTSlhMYzl6WGFlSFB4cFpaa2k3NDJUQVdMTEFkQ3FCTyUyRllDQnN5N1RWa0FTYTJqRW9Jck5xbUR2b2hqOEZVTm8xS0tlYjNiU1BENlZ5ZDBEQlp3NTFOdW93OHNVR0dHOXZJb05INERiQnlxSW1EVEV0Rzhzd0dTa0FaaVhvSElvRVg2VWdpVlBVV0xQbkJOWHM1TDl0NzFtdFppWUJKaXRjMEw0SDBsUDlydSUyQlQyOERPJTJCJTJGUGMxdmJ1T0hFJTJCTmxSdm5VQkh3bnB0SUh4QVp4TUJRTWZXZWpWOHVja2hsSXhaQ2hXJTJGb01mQ2dTcHBpSXNlbFpLQ1dpRnJuTU8xeHdOdFlOU2t3UURWWEUwWER4RWFtWWFHZlJZcXl6NW5URXhkd1BxVlNuSWo3UmxENUpHQUVHaGdNaGwyYUk2QlFXYTJOM0MwWXhGVUZFb09RU3UlMkJRdmRJMElKZ3VMOUpxWG1yWU5GRmJrekRGcXNtaGNlQzZKeGdmRDlSJTJGdzNyWjR0MmlHT0xqUUNZeVd6Mm1TTUw5T1l2WUNCRmIlMkJiaVNsRW5SblJkQTVKb0ZUeFdaMTk2dVlNRjh3MlZKdzdqUTQ5ODVQTzNVblNacHJaWlpkcjNQVmxNOTJwYWdjZzdKY3BlSVVvYjlkcjQ2bDExQUtINUpFU0lUZFk1Z2ozdG1CelpIdXE1emJFJTJCWWY1SndjR3VkbnIzSWVId1BuN1VQanZHZHhmcDh1WmtlMkIzZDZCOGI3JTJCZkh2d1YxdlozdHd0eW5mM3ZmZ1BGJTJCMkZDd1dzYzdjZ0NZaEJFYXZpblFhSDFLbFFNWXA0amxFendvbHhhJTJGaXBJJTJCMFhxS1Fjdm1JaHBNYlA3V0JzUnZ6YWxGdHZGcFdyU0ZJaG1HRHpNRUZVNDltQVBxNTRncXQwcE0ybGhXajZXZmJ2RU51c3VQOHhsMDIwMjdUenZCUmVkeHVuaVc3alVWaDJ5d3V5cyUyRm1JclN2SExZTHJ2ODVmSmhySjNGM3RuWmF4N3o5cjUzayUyRlp2ZEFTNWVINW9nM3U0U3hLcTk5cDhnTzdpUiUyQkN3clE2Y3BQSEhlS3J4MUtDWjczbyUyRnNpdzFMOXFKU3dESXd2UzJ0YWo0UG1ZSzdDVTJuNlJ3cmlYcXptQ3JPWXVnWHQ3T2x2dSUyQjdyR2pYZVhQekNWVEpBTElpQXp4bnZkanZLaVpjJTJCN1ppTUlNVmxSdkdyQnFWV0xwZjl3VVhzdHp5UjR6ekJrUk5LZWVqV3oxWHJCb3ZZa0dnUDdOU0ZDbW1jWkFlSW5ZbFFXUE5LaTdwTnRSemYwJTJCQ1QxRFFXYVQzR214dWZTUWhHeHk5ZWVGQnMlMkZ4VEklMkJ0ZSUyRmpWRUJyOEIlM0MlMkZkaWFncmFtJTNFJTNDJTJGbXhmaWxlJTNFiT4mFAAAGh5JREFUeF7tnWuoF0Ufx39WHtHSIC0L6Zi+MchLiqmkUpkkQV6K0MDLiw54zzpleeuoebCyi6akaWWEJuhBvPXCDNNCDZU45g0SQjPyRaFBGoqW+vCb55n/M2fc/e/sfy8zu/tdiOr8Z+fy+c7Mfvc3s7vNrl+/fp1wgAAIgAAIgAAIgAAIVEygGQxV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)

<a id="design-document-stream--producer"></a>

#### Producer

User can create following types of producer

> Synchronous Producer-Processing thread blocks until the producer has finished the event processing.

![Stream Sync Producer](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXMAAABwCAYAAADsWZCIAAAGbnRFWHRteGZpbGUAJTNDbXhmaWxlJTIwaG9zdCUzRCUyMmFwcC5kaWFncmFtcy5uZXQlMjIlMjBtb2RpZmllZCUzRCUyMjIwMjEtMDctMjVUMTUlM0E0MyUzQTA0LjI4NlolMjIlMjBhZ2VudCUzRCUyMjUuMCUyMChXaW5kb3dzJTIwTlQlMjAxMC4wJTNCJTIwV2luNjQlM0IlMjB4NjQpJTIwQXBwbGVXZWJLaXQlMkY1MzcuMzYlMjAoS0hUTUwlMkMlMjBsaWtlJTIwR2Vja28pJTIwQ2hyb21lJTJGOTEuMC40NDcyLjE2NCUyMFNhZmFyaSUyRjUzNy4zNiUyMiUyMGV0YWclM0QlMjJwLTkzWWctTTI2TTR1M2hqWWxZSyUyMiUyMHZlcnNpb24lM0QlMjIxNC45LjAlMjIlMjB0eXBlJTNEJTIyZGV2aWNlJTIyJTNFJTNDZGlhZ3JhbSUyMGlkJTNEJTIyLXRBSFh4Y2RhV0RrOEN5Q1ZMYWslMjIlMjBuYW1lJTNEJTIyUGFnZS0xJTIyJTNFM1ZoTGM5b3dFUDQxSE1QZ0I4UTVFaURwSVpreXphR1BDeU5zWWF1VnRSNVpnTW12cjJSTGZnSWhLVFJ0RHBsNFA3MjgzN2U3V3ROekpuRjJ6MUVTUFVLQWFjOGVCRm5QbWZaczI3SUdudnlua0YyQnVNTkJBWVNjQkhwU0JUeVJaNnhCTTIxTkFwdzJKZ29BS2tqU0JIMWdEUHVpZ1NIT1lkdWN0Z0xhUERWQkllNEFUejZpWGZRckNVUlVvSjd4UXVHZk1Ba2pVVHFzUjJKa0ptc2dqVkFBMnhya3pIck9oQU9JNGluT0pwZ3E4Z3d2eGJxN0E2UGxpM0hNeENrTFZ1UGQlMkZIbjV3M3NNRnclMkYlMkIzTjNZWHo1UHI0YkZMaHRFMTlwaCUyRmJKaVp4akFnU1JFbThCRkJDRXdSR2NWZXN0aHpRS3NqaGxJcTVyekFKQkkwSkxnVHl6RVRxdUwxZ0lrRkltWTZ0SGlUSFhRUWQ4MGxNS2ElMkIlMkZpSVElMkZyOUJlSWhGa2ZtdWFVQ01uUXh4Rmp3blZ6SE1VV0NiSnJ2Z1hRTWhlVzhpbWI1b0psJTJCQmV0MmglMkZVNUJ4JTJCbktmQU8lMkZSdk1CWkh4JTJCSUNXbU00aEpZSUFrME5MRUFKaVNaNlpNS1lrVkFOQ2tWNW5Wd1plb2phTHMxRGxhSDlGWWV0SGlJcyUyQnNDc1Z3QXVPVjFoU3JZalZXcWhOY1haY2pTNTdab0dyUTE3bnZIV3Q3VzJWUVFhS2FzbGpzTFB6N2U3ak8xajclMkJFUFE3ZGolMkZHTjJqbDR0S0tqajhLaXVxZlNxRGlERVFTRW15VUd1UTFvRGlsZlRwbHJZMDQ0V3Z0d2tRSmpDZmJTU2hhYVBrJTJGQm52N3JESnV6ZnM4Rzd2NGQyOUZPJTJGZUNjV2NCV04xSzByTHB5aE5pZCUyQmtYcnJPZDk5MEpjJTJCTjc4cm9ENDA1emVxRDA1MjJUcSUyRmdMMVptYTdDZjlScXJ3ejJzR3V6a0NxNVBtS3ZncUlrNmFvbDYwMUtydUlIMHF2cDEyOXFvYkhRT2JWUVEwZGtvVjc1MCUyQiUyQjNCWUJxb28xbG9FazFlUFhrZlZBJTJCRmJVUUVma3BRZnQxdVpTSTJoMkV0S0dGNFV2WmRnJTJGTmtsZXUxZVBPNjFjelpvNzk5cWF5eXJJOUJaTmxTdnh1UnpobnFVMFpFV1o3a2M2MDZTYXNxVHNwNGZXMTZzYnUwRGxEJTJCZDJxVE8yZ3BPbnBqYlhLdVd4dTFOYjkwYmVvMlpQOUZTcFdFbTlvMGV1JTJCVU91SDd6UkJKNGc2TmIyeDI4NTNHYVZKeHElMkZlV1o0VFNENThTeWFtTW5MdDdqUGpDc3IxTSUyRnZVVEZwNUJBNnV0d2MxcEdqZ1gwNkRiN3VhZFprY0k2Yk5vTmJwNUZ6d0JLciUyRjduQ2tEcHZSWkVVcGJrT2x6ZmF6NjJEMjZ4Q1FJOGslMkZ4ZlluUiUyRkR3JTJGZ3dST3F3NVp3NjRFN25uU1FKclZMeVJGJTJCYWwlMkJaM0ptdndFJTNEJTNDJTJGZGlhZ3JhbSUzRSUzQyUyRm14ZmlsZSUzReLzi6YAAB6PSURBVHhe7V1pkFRVlv5yqb2gqEVKFgvpZZBmDcARKUCjB6FHlJiObgeU5oehtvsGOK3Y2Io22NEitiJqq+MPFEWijekWGBkZtVEUN1pFGgmdVlGoKskqas31LRPnFq9IkqrK9zLvWzLr3LAiMfO+c+/97nlfnjzv3HN8uq7r4MYIMAKMACOQ0wj4mMxzev948owAI8AICASYzFkRGAFGgBHIAwSYzPNgE3kJjAAjwAgwmbMOMAKMACOQBwgwmefBJvISGAFGgBFgMmcd8BwCBw8exMKFC/Hxxx+fNLd58+bhueeeQ3V1tbQ5Nzc344YbbsDdd9+NMWPGSJPLghgBpxFgMncacR4vLQJE5jfddBMefvhh2wmWyTztdnCHHEGAyTxHNmogTbM/Mo9EIrj11luxZMkS1NfXC1juvfdefO9738PixYuxe/duzJw5U7x/9dVXY926deLfdM2IESNw1113if9ftWoVli9fLt5/4oknMGnSJGzevNn2L4+BtI+8VmcRYDJ3Fm8ezQQC6SxzcrX84x//wMqVK5FsWZNow6Kvq6vrIXCDtOlzIve9e/fi+uuvF+RdU1PDbhYTe8JdvI8Ak7n39yirGfp8vqyuz+biTA8X9+UzJ2uaCJysb7LGidQ/++wzbNy4UZD0Sy+9hDfffFP8u6SkRPSjz1avXo0VK1Zg1qxZwnpP/gJgMs9mh/laLyHAZO6l3bBhLkTmc+fOBb2uXbsW48aNs2GUbpH79+/H0qVLxVg7duxANmTen888mYxffPHFHhcLkfsvfvGLk9ZHD02ffvppQf6Ga4bJ3DYVYMEuIsBk7iL4TgxNxEqk+uCDD2LZsmWC0IlwZbdU+ca4mYyTzs1CMomca2tr8cUXX+CKK64Qvu5k90vyuKl+dibzTHaFr/E6AkzmXt+hLOeXTKrJlrMsK70vmXaTufGg03jISW6V1C8BIvzDhw/3uFnYMs9SmfhyTyPAZO7p7cl+cr2RqiwrvT852ZJ5b3HmyREnZF2T/5sIml6NlhzNYsSll5aWnhQBk2yZGw9K9+zZw9Es2asbS3ARASZzF8F3Yui+SDUbK93MtdmQuRO48BiMQL4hwGSebzuasp50pGrVSjfbP924eQ47L48RcBwBJnPHIXd2QDOkasbSNtMneWVmxnUWCR6NEchvBJjM83t/RZig2RDBvqxu4316pROTZpqVcc3I4z6MACPQPwJM5nmuIVZJNdkCv/baa7Fhw4aMYtStjpvn28DLYwRsR8BRMm9oaMD7778vsuFRGNmXX34Jeq+lpQVdXV1QFAXBYBBlZWWoqqrCsGHDMHr0aBFDTJEMZ599tniPm3kEMiVVssJffvllLFiwwLQ1PtDcLKzP5vWQe9qPgO1kvnPnTmzbtg30euTIEZxzzjmYPHkyxo4dK4h6+PDhIqUpETgRORE6ETuFj1F/IvwDBw7go48+wrvvviv6z5kzB/Pnzxev3NL89LLgZpGJZaZfIjLnYIcs1mc7UGWZMhCwhczJ6n7mmWewadMmQb4XX3wxKOZ32rRpWc/5gw8+EEfFyWoksr/ssstw+eWXc7a7PpB1i1TdGjdrBetFAOuzHaiyTNkISCXzd955B3/4wx/w6quv4sorrxR5MiZMmCB7zj3y9u3bh2effRZPPfUULrjgAtx8880499xzbRsvFwW7RapujStzj1ifZaLJsuxGQAqZk+VCR6d37dol8n5Q5RZymTjVyDWzfv16kX9k9uzZIrMeV43pRt8tUnVrXBk6x/osA0WW4TQCWZM5kTilJqWyW3feeafT8z9lvN/+9rdiLlSEgEh9oDe3SNWtcbPdb9bnbBHk691CIGMypwT/N954o/CJ/+53vxNpSL3SqHDBr371K+FTf+SRRzBlyhSvTM3xebhFqm6NmynArM+ZIsfXeQWBjMicfNRXXXUVHnvsMVxzzTVeWcsp83j88cdBsdJPPvmk8OEPxOYWqbo1biZ7zPqcCWp8jdcQsEzmd9xxB7Zu3SqiVWREp9gNCEW/ULTLRRddhDVr1tg9nOfku0Wqbo1rdQNYn60ixv29ioAlMqciAHRQ4vnnn0dFRYVX13TKvNra2nDppZeKA0dUdWYgNbdI1a1xrewt67MVtLiv1xEwTeYUZqiqqiDyXG1E6IFAQIQzDpRGpOpWM5sTxo35sT67gXr+j+nm/WaKzMmCCYfDOU3khhoRoVOxgoFmoef/bWR+hazP5rHintYQIDJ3q+ZuWjInnyLlUtm+fbu1VXm494UXXihyvQxEH7qHt8WRqbE+OwLzgB3EcC9mkmnUCmip8mncfsmcnvLTic633norp3zk6UAhH/rMmTPFidGBGuWSDqN8/Jz1OR931VtrSn5WZLUGgJmV9Fdzt08yp7jbqVOniiyHuRC1YgaI5D4U5UJZGD/88MMBHYduFbdc7e+0Pr/xxhv461//agqu8847D+eff76pvn11Yn3OCj5pF/f24F+Wld6fnH4t8/r6elEs18tx5NnuAMWhb9y4EVQEmFt+I+C0PtMp5HvuuccUqL/5zW/EqeVsG+tztghmf31fUVzZWOlmru2TzOlI8yeffIItW7ZkvzqPS7jkkkswceJEPvrv8X3KZnpu6LNB5masbrLKs7XMDXxYn7PRlPTXrl27Fr/85S8xaNCgXjunC8m1aqWb7d8rmVOSofHjx4viEV46op8e5sx60NF/Ssr16aefcnKuzCD09FVu6bNB5rKsbrMgsz6bRSqzfiUlJSJEe9myZVixYsUppJ6OzGlUM5a2mT7JK+iVzCn+lgpHeCFpVmZwW7+KknNRAYyBFH9uHaXcvMItfXaLzGmXWJ/t01UKCLn99tuhaZrISEo1cZNJ3QyZG7Pry+o2a433S+aUv3nhwoU4dOiQfWh4VHJdXR02b97M+dA9uj+ZTMtNfXaTzAkr1udMNMbcNVQZjUpdUissLDyJ1AcPHmy6gHqqlZ5tzd2TolkWLVqE6dOn45ZbbjG3Kht6xRu3ItFxCL7i7yM45EcIlpwGf7DYhpFOFvnQQw9hz549eOGFF2wfiwdwBgE39dkKmdODUhkPQJ1BlUfpDYGCggJRL/dPf/qTJTJPttKzrbnbQ+bkW5wxYwaampocLSxxAhgdWrwZyuGnoXQ1Qwl3IhFVgcLhKDp9GopqJiJYfBp8gSKquCBdo6jARW1tLd5++232nUtH13mBbuuzFTK3Ax3WZztQ7ZZZU1MjahTLsMxlzfIknzn5gSiXBuUmt6fp0DUF8dB7QMFpKCgfAV+wBD6fv3s4XYPa+jbUY7ughFu7yTzcCS0eQ9GQQUhEwvAXnYlA5RSUDJ+BYNlQ+PxyqxlRDnQC5f7777cHApbqGAL263P/S3GbzGl2rM/y1Y185nSKmB6CZuszlzm7k8icfGzbtm2zqWanDl2JINa4HcrRd6BEO6H5qxCsmIjiYfUoKK2EnghBbXkVWrQJaqQDSqQTSiQMXdPg92tQwhFoig41rqNw1L+hatIi+AuKZOIBqik6f/78AfnMQCqQHhBmrz6nX6AXyJz1Of0+We0hI5rF6phm+veQ+c6dO/HrX/9a+IzlNyLyTsS/+2+ox/ZCjUV6/rREHL6CMgwaNR5FFXXQtSjUaBvinc1ItIegxroQKChFNNQALaFBS+jQfINRXb8cpcPtKRRNzwzuu+8+zJkzRz4ULNERBOzVZ3NL8AKZ00xZn83tl9le2caZmx3Har8eMqfwGvIDyQ9H1KEnjkE99r9Q2/cfJ/GoeCX3ib+wCIXlAUCLo6h6KgLFg4QFr8c7EOs4hnDoOygd7VAjcahE5nEVgWGzcPrsaxAsGWx1vab6U1hXKBTCunXrTPXnTt5DwD59Nr9Wr5A567P5PZPR00pooozxDBk9ZD5hwgRbKgfpugql7V0ozf8Dn6pAjccFiavxGAKFxQgEY9CVMDQF8AfL4S8dgURbIxKdROARqHFVWORqQoUW15CIAyN/uhbFQ39wwtcuExEARmUi+onKLTcRsEufraDhFTJnfbaya9n3dZXMjxw5otOJT+PpbPbLOVmCFjuCxOH/RKLt/6AmAtD1AgRLKxDQ26AlItAVHZqidf8J4tahEXmLf2vdhB5XxWu8M4rBExegtv5SBMtq4PMXyJ6ukEdxpHQilCoTccstBKgSlp36bBYNr5A567PZHZPTz1Uy//Of/6xTgh678pXrWgKxpj1o/3gDtHgEOvwYNGoMfGoImhKHLsg7mczVHkucCFxNkEWvQokkoMYU+AIBDJ89DYU1Z8JXNgFF1ZPgLxgEnz8gZzcAUL5zSjBGcaPccguBv/zlL7BTn82i4SUyZ302u2vZ93OVzFetWqVHIhGsXr06+5X0JkFXEG89gPa//R7tR1qgtMcQKCpB9VnD4fdHocWVbktc6XankDWuqxTGCCiROJRoAkr0eJ/jpF8ytBK1U78PXU0g1qUirozEyHkrpc2fjufSU+uVK+XJlDY5FtQvApRUy1Z9Nom/l8ic9dnkpkno5iqZL168WJ83b55Id2tH0xOtiB3aiK5vdyMRVhDvTCDalkDZ6SNRXqmJiJVutwoROqBEgcLBfnEuKNoWh89XiHhnGNGWzhMWvAoUVw0W14SPdkDRSjD9969Jmz6lxd2xYwfnapGGqHOCKBeLnfpsdiVeInPWZ7O7ln0/V2uAzpgxQ6eDQlR5R3rTdagd+xD5v0cRa28TZC7+Ijoq6kYi4GuHGosej1QBju4Loeu7TgQKfKg6qxJVZ1VDiemIdwIdX4WghOPHLfhu/3q3e0aHXjAI0x94Xdr0qbISHbjgPOfSIJUmKF1oGOUtt02fLazCS2TO+mxh43K4q2/06NE6xeXake5WxJc3bkG88TXEuxI9ZA5fCQadXgY90QE1TgeCdDR8QFEsUQQK/fAX+FFQVoDqcXRStAjRYzHEOzWEG1q6H4YaRG4TmVMaUYozp1du3kIg3aEN0mO79NkKEl4ic9ZnKzuXu319FRUV+tdff21DjU8daud+KEeeQby9CfGu41Z5WEF53Rj4lQZosSgSYRWh/S2ItUYQKArAX+hHoCAAf9CP0tOHomb8KESbj6Lz20a0H+omf7vJnGqEjho1Cq2trbm7s3k683QpSIcMGQJ79NkaoF4ic9Zna3uXq719wWBQPAANBuXkOdGUCLRYCInQW/ArX0OJt0ALh0RYYSIcB3xlKKsuhJboElEqsdYEjn3eAvh1QeKBwm5C9wf8KBpSjSE/PAPR0Hfo/LbhZDInUqdwRj0IrawWM+79L2l7QEmKyAJMJBLSZLIgeQj0l4K0qqpKPACVpc+9zdpMObjXX39d1AB1ujhFb/NlfZane16WROkHdUqwJauFP1+DWPNXCBYWIlhSjmDpIHFASInH0fbtNwgWFCCAFugKRapo6GqIId4R7rbIDau80C9CDYMllSiqLEO8vRVdh4+i40iXODykKoBeOgzV5/wMtZN/jILyIQhIztPi5oMMWXsxkORkm4LUClZWUtZ6gcxpbW5FWVjBlftmh4B0yzz6+Z1AolEkyFLVAvgKq1FQWgFN6YQeb4YeC0OlcERFFT70SCgqIlfIT25Y5WSh61ohSoYOhxqPItbagmMHGxBri4uHniiqxMgFK1A1dkZ2q+/jarZkbIFVmtD+UpCyZX4qzKzP0lTP04Kk+8w79/0H9FijSGlLzV80CIXlxdDjrcItoh8/2UlkrsV1kbPcd9zFYvjLKbWtv3A4AkWFiHe0oKvxO7R81iiscopHLx/3rzjjJzegoGyILeCyj9EWWKUITZeClH3mp8LM+ixF9TwvRHo0S+v7t0DtaoJ+nMzp6H5ZDUWunErmdLS/oKwCauwYgkXdUSw+fxH8ZRMQLCoHlA5EWxrQ+ME+REId3aGIviKc8dO7MWRMvfjpaEfjp/92oCpHJkezWMeR9dk6Zrl4hU92nHlo13WIt3/XY5mTP7vijApA6YXMVR/8haUIlg6BluhA8dBx8AdLAB/V1SMuD6Hpgw/R2dgkQhKJzP2n/Qg/WHgfCgefZhveHJdrG7RZC+Y4c+sQsj5bxywXr/DJPgF67KP16Prmb1C6WkBHOouGVKL6h1WA2iaiV3Q6ti+Sa3VnQtT1AIqryTeeQEHFKBQNHiLiz+PtYTT//QDC3zV2+9gTGpSEjlH/vhaDzpwMf9CeJFu0iXxiLhdVuXvOfAL01L1jfXZOn+3yFphZgU92bhZyr1DYYbTpU3R8sRNa5AiqR2rQOpoQ69KAwWcg4O8QSba6feA6NM0HXaPY8jIRwdLV8I0oG6dEux94ihS4xw8InX7hClSN+zH8wUIz68uoD+eyyAg2T1zEuVlO3QbWZ+dUk8h87ty5wgVMvyLHjRtn2+D79+/H0qVLxViUfsRnZ9ZEqvlJDz6Vo9uROLoTsY44YhEfyk8fAS3SCC1Gx/P1HrIWSbZ6HpDSlwKR+InPidADZUNR97N7UTbyR7aBxFnmbIPWdsGcNfFUiFmfbVe7ngGMENAHH3wQy5YtA71SsRTZLVW+KE5hdz5zimpROr9C2967oUQiInoFgTKU1xSJikLJlrcZMicXTeXZizDiX65AoLBENkZCHucztwVWR4RyPvNTYWZ9dkT1xCDJ8fzJlrMsK70vmbZXGqLFUX6W2KFNaD/4CiLNMURbY1BUP6r+aTSKy+gQUKwXy1wVaW+J3EH/9RSuUFFQOxF1F9+GktNG2VJtiCuzOKf4do3ElYZOIMv6bJeW9S63t8NZsqz0/uQ4UAMU0DoPIvz5eoQbDiPSEkW0OYrIsRhOm3wWSqpi0JPIXImoQLASut6OYLEPSkxDZ0MHfOSKiasoOmM66uYvR8GgGluInLaHayY6q/x2jMY1QE+gyvpsh4b1LbOvk7bZWOlmru0hc7uqmetaHImmrYh98xIioXAPmdPJ0NrJw+APRIVfXCTOQiUq//l2UQ5OV8OINL2HyLfvoePQAUSPtqN0VD3O+MlSBEoG20bktEVczdxZ5bdjNLv02cpc7Uy01dHRgT/+8Y/CJ5uusT6nQ0ju5+nSJli10s327yFzWk5dXR22bdsG+okqrYnIljYoxz5B+Otd6Px6H7oamlExZiyKy9qhK9Hj0SwFKB51Ccp/uOBE+Tddh6bGkOhsRue3f0flmFnwB4vIKSVteqmCqIjz/PnzcejQIdvGYMHOIGCLPluYuh1kTiROFcHI/xoIBERCsf4a67OFDZPUNR2Z0zBmLG0zfZKnfBKZ33777ZRxSyT2l990UeJNjbSg6+s98Ef3CfeLqsVEdSEd5aicfj+C5UNtJet066KCFATK/fffn64rf+5xBOzV5/SLl0nmBomvW7dO3KNE5GvWrMHNN9/c70RYn9Pvk+weZsjcGLMvq9usNd4nmR88eBAzZsxAU1OTrelDaQJ6IgI1EkKs8T3EQ/sRqPg+Bo9bLBtXS/IoGVFtbS3efvttjBkzxtK13Nl7CDipz72tXgaZp5J4PB4XQ1F0SigU6hd01md3dNIKmada6ddeey02bNiQUYz6SZY5CV60aJHwGd9yyy3uIOHiqA899BD27NmDF154wcVZ8NAyEXBTn2WQ+c9//nNQ3Dzn1ZepFfbLyiSlOFnjL7/8MhYsWJBRXPopZP7OO+9g4cKFA9JnTD7WzZs349xzz7V/t3kERxBwU59lkHlfljml+W1ubu4XQ9ZnR1TslEGsWuayZnkKmZNgym0xduxY3HnnnbLG8bwcCt86cOAAnn32Wc/PlSdoDQG39FkGmRsrteozZ322piMye3uKzMnXOH78eNCrHUWeZQInQxalByUf+aeffsq+chmAekyGW/osk8xTSb2/aBbWZ3cV0FNkTlBQsqJPPvkEW7ZscRcZB0a/5JJLMHHiRKxcudKB0XgINxBwQ58NMj///PNBf/218847L22f5Ov7izNnfXZDw06M6Tkyp6nV19djyZIluOaaa9xFx8bRH3/8cZHudvfu3TaOwqK9gIDT+myQuZm1y6oTyvpsBm17+3iSzPfu3YupU6fi/fffx7Rp0+xFwAXplLPi7LPPxocffogpU6a4MAMe0kkEnNbnN954A/Rnppmx3tPJYX1Oh5Azn3uSzGnpTz31FKjmIlUqqaiocAYNB0ahmogzZ84Uhy6uvPJKB0bkIbyAAOuzF3Yhv+fgWTIn2O+44w58/PHH2L59e97sAuV3njRpkjhFx21gIcD6PLD22+nVeprMCYwrrrgC4XAYzz//vNPYSB/v0ksvRWlpKZ5++mnpsllgbiDA+pwb+5SLs/Q8mROoFK+rqmpOEzoROeW14HjyXLxN5M6Z9VkuniytGwFXa4DqFs6ekkVDlVzIQs8lHzr5yInIhw0bxhY533U9CLA+szLkEwI+K2Ru+NC3bt2KZ555JieiXIxKKxdddBH7yPNJcyWthXzorM+SwGQxriJgmcxpthQVcNVVV+Gxxx7zdBw6xd1SJrInn3ySo1ZcVTNvD8767O394dmZQyAjMifRFLd74403Yvjw4SIHupeO/tORZsrlfOTIETzyyCMcR25OFwZ0L9bnAb39ebH4jMncWD0dlV61ahXoxJsXknNRkiGay1133cVH9PNCRZ1dBOuzs3jzaPIQyJrMaSqUzIhugl27dmHp0qW44YYbbC9wkQwBJeJfv349KCfw7NmzBYlzgQl5SjLQJLE+D7Qdz4/1SiFzAwrKH00nRl999VXho6bwL6k1RVMwpxqHFGZIPs8LLrhAnOjkfOT5oZheWAXrsxd2gedgFgGpZG4MSpYNRbts2rRJ+NQvvvhizJs3T0r0C0Wn7NixQ1TlIJ/4ZZddhssvv5wtcbM7zv0sI8D6bBkyvsAFBGwh8+R17Ny5E9u2bQO9Evmec845mDx5siiAMXr0aEH2VNOwrKxMuGbIZdLV1SUqqVD/L7/8UhSO+Oijj/Duu++K/nPmzMH8+fPFKzdGwEkEWJ+dRJvHsoKA7WSePBk6cERZGCnXC1k7RNT0XktLiyBwInIidCJ2Ko1Fh3yI8Mn/TblUKMshvceNEfACAqzPXtgFnoOBgKNkzrAzAowAI8AI2IMAk7k9uLJURoARYAQcRYDJ3FG4eTBGgBFgBOxBgMncHlxZKiPACDACjiLAZO4o3DwYI8AIMAL2IMBkbg+uLJURYAQYAUcRYDJ3FG4ejBFgBBgBexBgMrcHV5bKCDACjICjCJgi8+eee07kWUludIhn8+bNfIze0e3iwWQjQAniKMNmcqPUE6TzdDI500bXv/nmm1i3bh1KSkoyFcPXMQKmETBN5qmKuXv3bmzcuJGV1TTU3NGLCBCZU6NMm0YjIqac+MnvWZ07k7lVxLh/tghkTOZ0HJ/yhlPq2Q0bNmD//v3CUqcshosXLxYpcQ2Lx3jPmGzyZ2+99Rbq6+sRiURw66234oknnhDd+nrfkJXaP3kM+qKZOXOmkHP11Vf3fOHQuKnzzBZAvj63EeiNzA1DZfXq1VixYgVaW1uFbpNOTpkypVc9JRQMvaNfrXPnzkV7e7vQvQceeEAUb6H7wtDbJUuWCL2nZuV+oDGofkBTUxOmT5/OxlRuq5/U2WdM5smWBynr4cOHexSLPiOrnV5DoRAWLlyIRx99VChvstWT+oVgWEiksNdff724gShLomElUfItKoBBBSheeeWVXt9PHs+48UaMGCGsLLppkucpFUkWlpMI9EbmxnvLly8XxG3oj0G8hg5RdSJDT+kzQ88NvaP30pG51fuB9NsYk3P256TK2TZp02Se6jNP9ium3hD0/4YlYtwA9GrcHMlWCb1PJE1WCxFuspVO/b766qtef/L29VM41f1D/0/zof70C8L4wrANURacUwj05jM3fs3RQojMZ82a1atVbVjZ9PmZZ555ktsxWQ/7sswN0rdyPxj3U7Y+/ZzaJJ6sKQRMk3l/D3OSyTtZwYmgqRnEe911151E2sYMDTKnPOXJrTeXjeF+6evnaaqvMtX6T/6SMYUQd8prBHqzzI0Fp7pEUo0OQweN+rfJ94gZMj/rrLMs3w+pXxp5vTm8OEsISCfzZAU3yDz1Z2tvlgiVmiMffH8/Helm6q1f8vv0MzT5wWyqZc5kbkk/8r6zFTJPJfdMLPPkL4T+LPO+7gcOPMh7lcx4gbaQeX8+8+Sbh6zmm266CQ8//DBefPHFHhcIvW/4H1977bUel02yz5xcJgYxJ7+fzmfOZJ6xruTlhVbI3DBUevOZ19TU9FjZvfnMk6+hh/PGL0yr9wPNgaPI8lIVs16ULWSe6gJJjjSxGrWS6oIxboK+3qex+4tmYTLPWmfySoBVMu9Lf1P1jqKyvvjiC9xzzz0Ih8OC6MmNeNttt4koF+PXqdX7gS3zvFI/qYsxReZSR2RhjAAjwAgwAtIRYDKXDikLZAQYAUbAeQSYzJ3HnEdkBBgBRkA6Akzm0iFlgYwAI8AIOI/A/wOxTwp5TbVvDQAAAABJRU5ErkJggg==)

In future Producer Types:

- Asynchronous Producer - Producer process the event in a sub-thread.

<a id="design-document-stream--consumer"></a>

#### Consumer

User can create following types of consumer

> Event-driven consumer-the processing of an incoming request is initiated when message binder call a method in consumer.

![Stream Event-Driven Consumer](assets/images/stream-event-driven-consumer-a629cc38b5a439f4423c277c92bdecf5_1a113d802397cdba.png)

In the Future

- Scheduled poll consumer
- Custom polling consumer

- [Overview of Event Streaming](#design-document-stream--overview-of-event-streaming)
- [Requirements](#design-document-stream--requirements)
  - [Functional Requirements](#design-document-stream--functional-requirements)
- [Design Details](#design-document-stream--design-details)
- [Architecture](#design-document-stream--architecture)
- [Design](#design-document-stream--design)
  - [EventMesh-Stream Component](#design-document-stream--eventmesh-stream-component)
- [EventMesh-Stream Component Interfaces](#design-document-stream--eventmesh-stream-component-interfaces)
  - [Component](#design-document-stream--component)
  - [EndPoint](#design-document-stream--endpoint)

---

<a id="sdk-java-intro"></a>

<!-- source_url: https://eventmesh.apache.org/docs/sdk-java/intro/ -->

<!-- page_index: 34 -->

# Installation

Version: v1.12.0

# Installation

[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.apache.eventmesh/eventmesh-sdk-java/badge.svg?style=for-the-badge)](https://maven-badges.herokuapp.com/maven-central/org.apache.eventmesh/eventmesh-sdk-java)

EventMesh SDK for Java is a collection of Java libraries to integrate EventMesh in a Java application. The SDK supports sending and receiving synchronous messages, asynchronous messages, and broadcast messages in TCP, HTTP, and gRPC protocols. The SDK implements EventMesh Message, CloudEvents, and OpenMessaging formats. The demo project is available in the [`eventmesh-example`](https://github.com/apache/eventmesh/tree/master/eventmesh-examples) module.

<div class="tabs-container tabList__CuJ"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_LNqP tabs__item--active" role="tab" tabindex="0">Gradle</li><li aria-selected="false" class="tabs__item tabItem_LNqP" role="tab" tabindex="-1">Maven</li></ul><div class="margin-top--md"><div class="tabItem_Ymn6" role="tabpanel"><p>    To install EventMesh SDK for Java with Gradle, declare <code>org.apache.eventmesh:eventmesh-sdk-java</code> as <code>implementation</code> in the dependencies block of the module's <code>build.gradle</code> file.</p><div class="language-gradle codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_biex"><pre class="prism-code language-gradle codeBlock_bY9V thin-scrollbar" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token keyword" style="color:#00009f">dependencies</span><span class="token plain"> </span><span class="token punctuation" style="color:#393A34">{</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain">  </span><span class="token keyword" style="color:#00009f">implementation</span><span class="token plain"> </span><span class="token string" style="color:#e3116c">'org.apache.eventmesh:eventmesh-sdk-java:1.10.0'</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain"></span><span class="token punctuation" style="color:#393A34">}</span> </span></code></pre><div class="buttonGroup__atx"></div></div></div></div><div class="tabItem_Ymn6" hidden="" role="tabpanel"><p>To install EventMesh SDK for Java with Maven, declare <code>org.apache.eventmesh:eventmesh-sdk-java</code> as a dependency in the dependencies block of the project's <code>pom.xml</code> file.</p><div class="language-xml codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_biex"><pre class="prism-code language-xml codeBlock_bY9V thin-scrollbar" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token tag punctuation" style="color:#393A34">&lt;</span><span class="token tag" style="color:#00009f">dependencies</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain">  </span><span class="token tag punctuation" style="color:#393A34">&lt;</span><span class="token tag" style="color:#00009f">dependency</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain">    </span><span class="token tag punctuation" style="color:#393A34">&lt;</span><span class="token tag" style="color:#00009f">groupId</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain">org.apache.eventmesh</span><span class="token tag punctuation" style="color:#393A34">&lt;/</span><span class="token tag" style="color:#00009f">groupId</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain">    </span><span class="token tag punctuation" style="color:#393A34">&lt;</span><span class="token tag" style="color:#00009f">artifactId</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain">eventmesh-sdk-java</span><span class="token tag punctuation" style="color:#393A34">&lt;/</span><span class="token tag" style="color:#00009f">artifactId</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain">    </span><span class="token tag punctuation" style="color:#393A34">&lt;</span><span class="token tag" style="color:#00009f">version</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain">1.10.0</span><span class="token tag punctuation" style="color:#393A34">&lt;/</span><span class="token tag" style="color:#00009f">version</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain">  </span><span class="token tag punctuation" style="color:#393A34">&lt;/</span><span class="token tag" style="color:#00009f">dependency</span><span class="token tag punctuation" style="color:#393A34">&gt;</span><span class="token plain"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain"></span><span class="token tag punctuation" style="color:#393A34">&lt;/</span><span class="token tag" style="color:#00009f">dependencies</span><span class="token tag punctuation" style="color:#393A34">&gt;</span> </span></code></pre><div class="buttonGroup__atx"></div></div></div></div></div></div>

---

<a id="sdk-java-http"></a>

<!-- source_url: https://eventmesh.apache.org/docs/sdk-java/http/ -->

<!-- page_index: 35 -->

# HTTP Protocol

Version: v1.12.0

# HTTP Protocol

EventMesh SDK for Java implements the HTTP producer and consumer of asynchronous messages. Both the producer and consumer require an instance of `EventMeshHttpClientConfig` class that specifies the configuration of EventMesh HTTP client. The `liteEventMeshAddr`, `userName`, and `password` fields should match the `eventmesh.properties` file of EventMesh Runtime.

```java
import org.apache.eventmesh.client.http.conf.EventMeshHttpClientConfig;
import org.apache.eventmesh.common.utils.IPUtils;
import org.apache.eventmesh.common.utils.ThreadUtils;

public class HTTP {
  public static void main(String[] args) throws Exception {
    EventMeshHttpClientConfig eventMeshClientConfig = EventMeshHttpClientConfig.builder()
      .liteEventMeshAddr("localhost:10105")
      .producerGroup("TEST_PRODUCER_GROUP")
      .env("env")
      .idc("idc")
      .ip(IPUtils.getLocalAddress())
      .sys("1234")
      .pid(String.valueOf(ThreadUtils.getPID()))
      .userName("eventmesh")
      .password("password")
      .build();
      /* ... */
  }
}
```

<a id="sdk-java-http--http-consumer"></a>

## HTTP Consumer

The `EventMeshHttpConsumer` class implements the `heartbeat`, `subscribe`, and `unsubscribe` methods. The `subscribe` method accepts a list of `SubscriptionItem` that defines the topics to be subscribed and a callback URL.

```java
import org.apache.eventmesh.client.http.consumer.EventMeshHttpConsumer;
import org.apache.eventmesh.common.protocol.SubscriptionItem;
import org.apache.eventmesh.common.protocol.SubscriptionMode;
import org.apache.eventmesh.common.protocol.SubscriptionType;
import com.google.common.collect.Lists;

public class HTTP {
  final String url = "http://localhost:8080/callback";
  final List<SubscriptionItem> topicList = Lists.newArrayList(
    new SubscriptionItem("eventmesh-async-topic", SubscriptionMode.CLUSTERING, SubscriptionType.ASYNC)
  );

  public static void main(String[] args) throws Exception {
    /* ... */
    eventMeshHttpConsumer = new EventMeshHttpConsumer(eventMeshClientConfig);
    eventMeshHttpConsumer.heartBeat(topicList, url);
    eventMeshHttpConsumer.subscribe(topicList, url);
    /* ... */
    eventMeshHttpConsumer.unsubscribe(topicList, url);
  }
}
```

The EventMesh Runtime will send a POST request that contains the message in the [CloudEvents format](https://github.com/cloudevents/spec) to the callback URL. The [`SubController.java` file](https://github.com/apache/eventmesh/blob/master/eventmesh-examples/src/main/java/org/apache/eventmesh/http/demo/sub/controller/SubController.java) implements a Spring Boot controller that receives and parses the callback messages.

<a id="sdk-java-http--http-producer"></a>

## HTTP Producer

The `EventMeshHttpProducer` class implements the `publish` method. The `publish` method accepts the message to be published and an optional timeout value. The message should be an instance of either of these classes:

- `org.apache.eventmesh.common.EventMeshMessage`
- `io.cloudevents.CloudEvent`
- `io.openmessaging.api.Message`

```java
import org.apache.eventmesh.client.http.producer.EventMeshHttpProducer;
import org.apache.eventmesh.client.tcp.common.EventMeshCommon;
import org.apache.eventmesh.common.Constants;
import org.apache.eventmesh.common.utils.JsonUtils;

import io.cloudevents.CloudEvent;
import io.cloudevents.core.builder.CloudEventBuilder;

public class HTTP {
  public static void main(String[] args) throws Exception {
    /* ... */
    EventMeshHttpProducer eventMeshHttpProducer = new EventMeshHttpProducer(eventMeshClientConfig);
    Map<String, String> content = new HashMap<>();
    content.put("content", "testAsyncMessage");

    CloudEvent event = CloudEventBuilder.v1()
      .withId(UUID.randomUUID().toString())
      .withSubject("eventmesh-async-topic")
      .withSource(URI.create("/"))
      .withDataContentType("application/cloudevents+json")
      .withType(EventMeshCommon.CLOUD_EVENTS_PROTOCOL_NAME)
      .withData(JsonUtils.serialize(content).getBytes(StandardCharsets.UTF_8))
      .withExtension(Constants.EVENTMESH_MESSAGE_CONST_TTL, String.valueOf(4 * 1000))
      .build();
    eventMeshHttpProducer.publish(event);
  }
}
```

<a id="sdk-java-http--using-curl-command"></a>

## Using Curl Command

You can also publish/subscribe event without EventMesh SDK.

<a id="sdk-java-http--publish"></a>

### Publish

```shell
curl -H "Content-Type:application/json" -X POST -d '{"name": "admin", "pass":"12345678"}' http://127.0.0.1:10105/eventmesh/publish/TEST-TOPIC-HTTP-ASYNC
```

After you start the EventMesh Runtime server, you can use the curl command publish the event to the specific topic with the HTTP POST method and the package body must be in JSON format. The publish url like (<http://127.0.0.1:10105/eventmesh/publish/TEST-TOPIC-HTTP-ASYNC>), and you will get the publish successful result.

<a id="sdk-java-http--subscribe"></a>

### Subscribe

```shell
curl -H "Content-Type:application/json" -X POST -d '{"url": "http://127.0.0.1:8088/sub/test", "consumerGroup":"TEST-GROUP", "topic":[{"mode":"CLUSTERING","topic":"TEST-TOPIC-HTTP-ASYNC","type":"ASYNC"}]}' http://127.0.0.1:10105/eventmesh/subscribe/local
```

After you start the EventMesh Runtime server, you can use the curl command to subscribe the specific topic list with the HTTP POST method, and the package body must be in JSON format. The subscribe url like (<http://127.0.0.1:10105/eventmesh/subscribe/local>), and you will get the subscribe successful result. You should pay attention to the `url` field in the package body, which means you need to set up an HTTP service at the specified URL.

You can see the example in the `eventmesh-examples` module.

- [HTTP Consumer](#sdk-java-http--http-consumer)
- [HTTP Producer](#sdk-java-http--http-producer)
- [Using Curl Command](#sdk-java-http--using-curl-command)
  - [Publish](#sdk-java-http--publish)
  - [Subscribe](#sdk-java-http--subscribe)

---

<a id="sdk-java-tcp"></a>

<!-- source_url: https://eventmesh.apache.org/docs/sdk-java/tcp/ -->

<!-- page_index: 36 -->

# TCP Protocol

Version: v1.12.0

# TCP Protocol

EventMesh SDK for Java implements the TCP producer and consumer of synchronous, asynchronous, and broadcast messages. Both the producer and consumer require an instance of `EventMeshTCPClientConfig` class that specifies the configuration of EventMesh TCP client. The `host` and `port` fields should match the `eventmesh.properties` file of EventMesh Runtime.

```java
import org.apache.eventmesh.client.tcp.conf.EventMeshTCPClientConfig;
import org.apache.eventmesh.client.tcp.common.ReceiveMsgHook;
import io.cloudevents.CloudEvent;

public class AsyncSubscribe implements ReceiveMsgHook<CloudEvent> {
  public static void main(String[] args) throws InterruptedException {
    EventMeshTCPClientConfig eventMeshTcpClientConfig = EventMeshTCPClientConfig.builder()
      .host(eventMeshIp)
      .port(eventMeshTcpPort)
      .userAgent(userAgent)
      .build();
    /* ... */
  }
}
```

<a id="sdk-java-tcp--tcp-consumer"></a>

## TCP Consumer

The consumer should implement the `ReceiveMsgHook` class, which is defined in [`ReceiveMsgHook.java`](https://github.com/apache/eventmesh/blob/master/eventmesh-sdk-java/src/main/java/org/apache/eventmesh/client/tcp/common/ReceiveMsgHook.java).

```java
public interface ReceiveMsgHook<ProtocolMessage> {
  Optional<ProtocolMessage> handle(ProtocolMessage msg);
}
```

The `EventMeshTCPClient` class implements the `subscribe` method. The `subscribe` method accepts the topic, the `SubscriptionMode`, and the `SubscriptionType`. The `handle` method will be invoked when the consumer receives a message from the topic it subscribes. If the `SubscriptionType` is `SYNC`, the return value of `handle` will be sent back to the producer.

```java
import org.apache.eventmesh.client.tcp.EventMeshTCPClient;
import org.apache.eventmesh.client.tcp.EventMeshTCPClientFactory;
import org.apache.eventmesh.client.tcp.common.ReceiveMsgHook;
import org.apache.eventmesh.common.protocol.SubscriptionMode;
import org.apache.eventmesh.common.protocol.SubscriptionType;
import io.cloudevents.CloudEvent;

public class TCPConsumer implements ReceiveMsgHook<CloudEvent> {
  public static TCPConsumer handler = new TCPConsumer();
  private static EventMeshTCPClient<CloudEvent> client;

  public static void main(String[] args) throws Exception {
    client = EventMeshTCPClientFactory.createEventMeshTCPClient(
      eventMeshTcpClientConfig,
      CloudEvent.class
    );
    client.init();

    client.subscribe(
      "eventmesh-sync-topic",
      SubscriptionMode.CLUSTERING,
      SubscriptionType.SYNC
    );

    client.registerSubBusiHandler(handler);
    client.listen();
  }

  @Override
  public Optional<CloudEvent> handle(CloudEvent message) {
    log.info("Messaged received: {}", message);
    return Optional.of(message);
  }
}
```

<a id="sdk-java-tcp--tcp-producer"></a>

## TCP Producer

<a id="sdk-java-tcp--asynchronous-producer"></a>

### Asynchronous Producer

The `EventMeshTCPClient` class implements the `publish` method. The `publish` method accepts the message to be published and an optional timeout value and returns the response message from the consumer.

```java
/* ... */
client = EventMeshTCPClientFactory.createEventMeshTCPClient(eventMeshTcpClientConfig, CloudEvent.class);
client.init();

CloudEvent event = CloudEventBuilder.v1()
  .withId(UUID.randomUUID().toString())
  .withSubject(ExampleConstants.EVENTMESH_GRPC_ASYNC_TEST_TOPIC)
  .withSource(URI.create("/"))
  .withDataContentType(ExampleConstants.CLOUDEVENT_CONTENT_TYPE)
  .withType(EventMeshCommon.CLOUD_EVENTS_PROTOCOL_NAME)
  .withData(JsonUtils.serialize(content).getBytes(StandardCharsets.UTF_8))
  .withExtension(Constants.EVENTMESH_MESSAGE_CONST_TTL, String.valueOf(4 * 1000))
  .build();
client.publish(event, 1000);
```

<a id="sdk-java-tcp--synchronous-producer"></a>

### Synchronous Producer

The `EventMeshTCPClient` class implements the `rr` method. The `rr` method accepts the message to be published and an optional timeout value and returns the response message from the consumer.

```java
/* ... */
client = EventMeshTCPClientFactory.createEventMeshTCPClient(eventMeshTcpClientConfig, CloudEvent.class);
client.init();

CloudEvent event = CloudEventBuilder.v1()
  .withId(UUID.randomUUID().toString())
  .withSubject(ExampleConstants.EVENTMESH_GRPC_ASYNC_TEST_TOPIC)
  .withSource(URI.create("/"))
  .withDataContentType(ExampleConstants.CLOUDEVENT_CONTENT_TYPE)
  .withType(EventMeshCommon.CLOUD_EVENTS_PROTOCOL_NAME)
  .withData(JsonUtils.serialize(content).getBytes(StandardCharsets.UTF_8))
  .withExtension(Constants.EVENTMESH_MESSAGE_CONST_TTL, String.valueOf(4 * 1000))
  .build();

Package response = client.rr(event, 1000);
CloudEvent replyEvent = EventFormatProvider
  .getInstance()
  .resolveFormat(JsonFormat.CONTENT_TYPE)
  .deserialize(response.getBody().toString().getBytes(StandardCharsets.UTF_8));
```

- [TCP Consumer](#sdk-java-tcp--tcp-consumer)
- [TCP Producer](#sdk-java-tcp--tcp-producer)
  - [Asynchronous Producer](#sdk-java-tcp--asynchronous-producer)
  - [Synchronous Producer](#sdk-java-tcp--synchronous-producer)

---

<a id="sdk-java-grpc"></a>

<!-- source_url: https://eventmesh.apache.org/docs/sdk-java/grpc/ -->

<!-- page_index: 37 -->

# gRPC Protocol

Version: v1.12.0

# gRPC Protocol

EventMesh SDK for Java implements the gRPC producer and consumer of synchronous, asynchronous, and broadcast messages. Both the producer and consumer require an instance of `EventMeshGrpcClientConfig` class that specifies the configuration of EventMesh gRPC client. The `liteEventMeshAddr`, `userName`, and `password` fields should match the `eventmesh.properties` file of EventMesh Runtime.

```java
import org.apache.eventmesh.client.grpc.config.EventMeshGrpcClientConfig;
import org.apache.eventmesh.client.grpc.consumer.ReceiveMsgHook;
import io.cloudevents.CloudEvent;

public class CloudEventsAsyncSubscribe implements ReceiveMsgHook<CloudEvent> {
  public static void main(String[] args) throws InterruptedException {
    EventMeshGrpcClientConfig eventMeshClientConfig = EventMeshGrpcClientConfig.builder()
      .serverAddr("localhost")
      .serverPort(10205)
      .consumerGroup(ExampleConstants.DEFAULT_EVENTMESH_TEST_CONSUMER_GROUP)
      .env("env").idc("idc")
      .sys("1234").build();
    /* ... */
  }
}
```

<a id="sdk-java-grpc--grpc-consumer"></a>

## gRPC Consumer

<a id="sdk-java-grpc--stream-consumer"></a>

### Stream Consumer

The EventMesh Runtime sends the message from producers to the stream consumer as a series of event streams. The consumer should implement the `ReceiveMsgHook` class, which is defined in [`ReceiveMsgHook.java`](https://github.com/apache/eventmesh/blob/master/eventmesh-sdk-java/src/main/java/org/apache/eventmesh/client/grpc/consumer/ReceiveMsgHook.java).

```java
public interface ReceiveMsgHook<T> {
    Optional<T> handle(T msg) throws Throwable;
    String getProtocolType();
}
```

The `EventMeshGrpcConsumer` class implements the `registerListener`, `subscribe`, and `unsubscribe` methods. The `subscribe` method accepts a list of `SubscriptionItem` that defines the topics to be subscribed to. The `registerListener` accepts an instance of a class that implements the `ReceiveMsgHook`. The `handle` method will be invoked when the consumer receives a message from the topic it subscribes. If the `SubscriptionType` is `SYNC`, the return value of `handle` will be sent back to the producer.

```java
import org.apache.eventmesh.client.grpc.consumer.EventMeshGrpcConsumer;
import org.apache.eventmesh.client.grpc.consumer.ReceiveMsgHook;
import org.apache.eventmesh.client.tcp.common.EventMeshCommon;
import org.apache.eventmesh.common.protocol.SubscriptionItem;
import org.apache.eventmesh.common.protocol.SubscriptionMode;
import org.apache.eventmesh.common.protocol.SubscriptionType;
import io.cloudevents.CloudEvent;

public class CloudEventsAsyncSubscribe implements ReceiveMsgHook<CloudEvent> {
    public static CloudEventsAsyncSubscribe handler = new CloudEventsAsyncSubscribe();
    public static void main(String[] args) throws InterruptedException {
        /* ... */
        SubscriptionItem subscriptionItem = new SubscriptionItem(
          "eventmesh-async-topic",
          SubscriptionMode.CLUSTERING,
          SubscriptionType.ASYNC
        );
        EventMeshGrpcConsumer eventMeshGrpcConsumer = new EventMeshGrpcConsumer(eventMeshClientConfig);

        eventMeshGrpcConsumer.init();
        eventMeshGrpcConsumer.registerListener(handler);
        eventMeshGrpcConsumer.subscribe(Collections.singletonList(subscriptionItem));
        /* ... */
        eventMeshGrpcConsumer.unsubscribe(Collections.singletonList(subscriptionItem));
    }

    @Override
    public Optional<CloudEvent> handle(CloudEvent message) {
      log.info("Messaged received: {}", message);
      return Optional.empty();
    }

    @Override
    public String getProtocolType() {
      return EventMeshCommon.CLOUD_EVENTS_PROTOCOL_NAME;
    }
}
```

<a id="sdk-java-grpc--webhook-consumer"></a>

### Webhook Consumer

The `subscribe` method of the `EventMeshGrpcConsumer` class accepts a list of `SubscriptionItem` that defines the topics to be subscribed and an optional callback URL. If the callback URL is provided, the EventMesh Runtime will send a POST request that contains the message in the [CloudEvents format](https://github.com/cloudevents/spec) to the callback URL. The [`SubController.java` file](https://github.com/apache/eventmesh/blob/master/eventmesh-examples/src/main/java/org/apache/eventmesh/grpc/sub/app/controller/SubController.java) implements a Spring Boot controller that receives and parses the callback messages.

```java
import org.apache.eventmesh.client.grpc.consumer.EventMeshGrpcConsumer;
import org.apache.eventmesh.client.grpc.consumer.ReceiveMsgHook;
import org.apache.eventmesh.client.tcp.common.EventMeshCommon;
import org.apache.eventmesh.common.protocol.SubscriptionItem;
import org.apache.eventmesh.common.protocol.SubscriptionMode;
import org.apache.eventmesh.common.protocol.SubscriptionType;

@Component
public class SubService implements InitializingBean {
  final String url = "http://localhost:8080/callback";

  public void afterPropertiesSet() throws Exception {
    /* ... */
    eventMeshGrpcConsumer = new EventMeshGrpcConsumer(eventMeshClientConfig);
    eventMeshGrpcConsumer.init();

    SubscriptionItem subscriptionItem = new SubscriptionItem(
      "eventmesh-async-topic",
      SubscriptionMode.CLUSTERING,
      SubscriptionType.ASYNC
    );

    eventMeshGrpcConsumer.subscribe(Collections.singletonList(subscriptionItem), url);
    /* ... */
    eventMeshGrpcConsumer.unsubscribe(Collections.singletonList(subscriptionItem), url);
  }
}
```

<a id="sdk-java-grpc--grpc-producer"></a>

## gRPC Producer

<a id="sdk-java-grpc--asynchronous-producer"></a>

### Asynchronous Producer

The `EventMeshGrpcProducer` class implements the `publish` method. The `publish` method accepts the message to be published and an optional timeout value. The message should be an instance of either of these classes:

- `org.apache.eventmesh.common.EventMeshMessage`
- `io.cloudevents.CloudEvent`

```java
/* ... */
EventMeshGrpcProducer eventMeshGrpcProducer = new EventMeshGrpcProducer(eventMeshClientConfig);
eventMeshGrpcProducer.init();

Map<String, String> content = new HashMap<>();
content.put("content", "testAsyncMessage");

CloudEvent event = CloudEventBuilder.v1()
  .withId(UUID.randomUUID().toString())
  .withSubject(ExampleConstants.EVENTMESH_GRPC_ASYNC_TEST_TOPIC)
  .withSource(URI.create("/"))
  .withDataContentType(ExampleConstants.CLOUDEVENT_CONTENT_TYPE)
  .withType(EventMeshCommon.CLOUD_EVENTS_PROTOCOL_NAME)
  .withData(JsonUtils.serialize(content).getBytes(StandardCharsets.UTF_8))
  .withExtension(Constants.EVENTMESH_MESSAGE_CONST_TTL, String.valueOf(4 * 1000))
  .build();
eventMeshGrpcProducer.publish(event);
```

<a id="sdk-java-grpc--synchronous-producer"></a>

### Synchronous Producer

The `EventMeshGrpcProducer` class implements the `requestReply` method. The `requestReply` method accepts the message to be published and an optional timeout value. The method returns the message returned from the consumer. The message should be an instance of either of these classes:

- `org.apache.eventmesh.common.EventMeshMessage`
- `io.cloudevents.CloudEvent`

<a id="sdk-java-grpc--batch-producer"></a>

### Batch Producer

The `EventMeshGrpcProducer` class overloads the `publish` method, which accepts a list of messages to be published and an optional timeout value. The messages in the list should be an instance of either of these classes:

- `org.apache.eventmesh.common.EventMeshMessage`
- `io.cloudevents.CloudEvent`

```java
/* ... */
List<CloudEvent> cloudEventList = new ArrayList<>();
for (int i = 0; i < 5; i++) {
  CloudEvent event = CloudEventBuilder.v1()
    .withId(UUID.randomUUID().toString())
    .withSubject(ExampleConstants.EVENTMESH_GRPC_ASYNC_TEST_TOPIC)
    .withSource(URI.create("/"))
    .withDataContentType(ExampleConstants.CLOUDEVENT_CONTENT_TYPE)
    .withType(EventMeshCommon.CLOUD_EVENTS_PROTOCOL_NAME)
    .withData(JsonUtils.serialize(content).getBytes(StandardCharsets.UTF_8))
    .withExtension(Constants.EVENTMESH_MESSAGE_CONST_TTL, String.valueOf(4 * 1000))
    .build();

  cloudEventList.add(event);
}

eventMeshGrpcProducer.publish(cloudEventList);
/* ... */
```

- [gRPC Consumer](#sdk-java-grpc--grpc-consumer)
  - [Stream Consumer](#sdk-java-grpc--stream-consumer)
  - [Webhook Consumer](#sdk-java-grpc--webhook-consumer)
- [gRPC Producer](#sdk-java-grpc--grpc-producer)
  - [Asynchronous Producer](#sdk-java-grpc--asynchronous-producer)
  - [Synchronous Producer](#sdk-java-grpc--synchronous-producer)
  - [Batch Producer](#sdk-java-grpc--batch-producer)

---

<a id="upgrade-guide-upgrade-guide"></a>

<!-- source_url: https://eventmesh.apache.org/docs/upgrade-guide/upgrade-guide/ -->

<!-- page_index: 38 -->

# EventMesh Upgrade Guide

Version: v1.12.0

# EventMesh Upgrade Guide

> This article briefly introduces the precautions for upgrading EventMesh from version 1.2.0 to the latest version.

<a id="upgrade-guide-upgrade-guide--1-precautions"></a>

## 1. Precautions

**If you are using EventMesh for the first time, you can ignore this chapter.**

<a id="upgrade-guide-upgrade-guide--2-service-upgrade-installation"></a>

## 2. Service upgrade installation

The upgrade and startup of the EventMesh Runtime module can be done in accordance with the [Deployment Guide](#instruction-runtime).

For differences and changes between versions, please refer to the [Release Notes](https://eventmesh.apache.org/events/release-notes) of different versions. Compatibility between versions can be achieved.

If you need to use the latest features, follow the release note to upgrade to the corresponding version That’s it, and different plug-in module components can be packaged and configured separately. You can refer to the corresponding [Feature design documents and Guidelines](https://eventmesh.apache.org/docs/design-document/).

- [1. Precautions](#upgrade-guide-upgrade-guide--1-precautions)
- [2. Service upgrade installation](#upgrade-guide-upgrade-guide--2-service-upgrade-installation)

---
