# Output Templates

Reference templates for generating course output files. Replace placeholders (`{...}`) with actual content.

---

## Template 1: Full Chinese Transcript

**Folder:** `01-Complete-Transcript/`
**Filename:** `L01-{lecture-title}.md`

```markdown
# L01: Distributed Systems Overview - 完整中文文字记录

MIT 6.824 2020 | Lecture 1 | Instructor: Robert Morris

---

[00:00] 今天我们开始分布式系统这门课。首先，什么是 distributed system(分布式系统)?

[00:45] 简单来说，分布式系统是一组合作的 computer(计算机)，通过网络通信来完成共同的任务，对外表现为单一系统。

[01:30] 一个经典例子是 Google 搜索引擎。当你在浏览器输入关键词，请求被发送到许多服务器，每个服务器处理一部分数据，最终汇聚成结果。这就是 MapReduce(映射归约) 的典型应用。

[02:15] Map 阶段将输入数据分割成小块，每块由一个 map task(映射任务) 处理，输出 key-value pairs(键值对)。然后系统将这些键值对按照 key 进行 shuffle(洗牌/分组)，发送给 reduce tasks(归约任务)。

```python
def map(key, value):
    for word in value.split():
        emit(word, 1)

def reduce(key, values):
    emit(key, sum(values))
```

[03:20] 程序员只需写 map 和 reduce 函数，系统自动处理并行化、fault tolerance(容错)、data distribution(数据分布) 等复杂问题。

[04:00] 接下来是 RPC(Remote Procedure Call，远程过程调用)。RPC 让程序像调用本地函数一样调用远程机器上的函数。框架负责 marshalling(编组/序列化) 参数、发送网络请求、处理错误。

[05:00] 一个关键问题：如何处理 failures(故障)? 网络可能丢包，服务器可能宕机。RPC 系统通常提供三种语义：至少一次(at-least-once)、至多一次(at-most-once) 和恰好一次(exactly-once)。

[06:00] 总结：分布式系统无处不在，MapReduce 提供简洁的编程模型，RPC 是基础通信机制，而处理故障是核心挑战。

---

*学习辅助材料 - 非官方课程材料*
```

---

## Template 2: Key Points Summary

**Folder:** `02-Key-Points/`
**Filename:** `L01-{lecture-title}.md`

```markdown
# L01: Distributed Systems Overview - 重点概括

MIT 6.824 2020 | Lecture 1

## 核心概念

- **分布式系统定义**: 一组通过网络通信、协同完成任务的计算机,对外表现为单一系统
- **主要挑战**: 并发性(concurrency)、故障处理(fault tolerance)、异构性(heterogeneity)、一致性(consistency)
- **MapReduce 模型**: Google 提出的分布式计算框架,分为 Map 和 Reduce 两个阶段

## MapReduce 详解

| 阶段 | 输入 | 输出 | 说明 |
|------|------|------|------|
| Map | (k1, v1) | List(k2, v2) | 处理原始数据,产出中间键值对 |
| Shuffle | - | - | 系统自动按 key 分组 |
| Reduce | (k2, List(v2)) | List(k3, v3) | 聚合相同 key 的数据 |

### 关键设计决策

1. **数据局部性**: 将计算移动到数据所在节点,减少网络传输
2. **容错机制**: 通过重新执行失败任务来应对故障,而非显式恢复中间状态
3. **水平扩展**: 增加机器即可线性提升吞吐量

```go
// MapReduce 的容错逻辑示意
func handleFailure(task Task) {
    // 重新调度失败的任务到可用 worker
    // 已完成的 map 任务需要重新执行? 不需要
    // 因为 map 输出存储在本地磁盘
    // 已完成的 reduce 任务需要重新执行? 不需要
    // 因为 reduce 输出已写入全局文件系统
}
```

## 与其他概念的联系

- **RPC**: MapReduce 依赖 RPC 进行 worker 之间的通信
- **GFS**: MapReduce 的输入输出存储在 GFS(Google File System) 上
- **Bigtable**: MapReduce 常用于处理 Bigtable 中的大规模数据

---

*学习辅助材料 - 非官方课程材料*
```

---

## Template 3: Beginner-Friendly Explanation

**Folder:** `03-Beginner-Explanation/`
**Filename:** `L01-{lecture-title}.md`

```markdown
# L01: Distributed Systems Overview - 通俗理解

MIT 6.824 2020 | Lecture 1

## 我为什么要关心这个?

你每天都在使用分布式系统。刷抖音、逛淘宝、用微信,背后都是成千上万台服务器在协同工作。当你点赞一条朋友圈时,你的请求可能经过几十台机器处理后才会显示在朋友手机上。

## 一个类比: 饭店厨房

想象一家大型饭店的后厨:

- **单机系统**: 一个厨师负责所有菜品。简单但容量有限,厨师生病 = 饭店停业
- **分布式系统**: 多个厨师各司其职,切菜的切菜,炒菜的炒菜。某个厨师请假,其他人继续工作
- **MapReduce**: 好比"接到100桌订单"。经理(coordinator) 把订单分给多个厨师(workers),然后汇总结果

## 通俗版本

**分布式系统** = 一群计算机(节点)通过网络连接,一起干活,让你感觉像在用一台超级计算机。

**MapReduce** = 一种"分而治之"的方法:
1. **Map(分)**: 把大任务拆成小任务,分配给多台机器并行处理
2. **Reduce(合)**: 把各机器的中间结果汇总成最终答案

**RPC** = 网络版的"打电话"。你的程序想调用另一台机器上的函数,就像打电话让对方帮忙做事。

## 专业化版本

**分布式系统**由多个自治节点组成,节点间通过消息传递进行通信和协调,对外呈现单一系统映像。设计目标是可扩展性(scalability)、可用性(availability)、一致性(consistency)和容错性(fault tolerance)。

**MapReduce**是函数式编程思想在大规模数据处理中的具体落地。纯函数式的 map 和 reduce 操作天然支持并行化,因为 map 之间无依赖,且 reduce 在不同 key 之间也无依赖。

## 一句话总结

分布式系统让多台计算机像一个团队一样协作处理大规模问题,而 MapReduce 提供了一种简单优雅的方式让它们分工合作。

---

*学习辅助材料 - 非官方课程材料*
```

---

## Template 4: Lab Walkthrough

**Folder:** `04-Lab-Walkthrough/`
**Filename:** `Lab01-{lab-name}.md`

```markdown
# Lab 01: MapReduce - 实验带做

MIT 6.824 2020

## 实验目标

- 实现一个简化版的 MapReduce 系统
- 理解 coordinator-worker 架构的工作原理
- 掌握 Go 语言的 RPC 编程和并发控制

## 前置要求

- 完成 Lecture 1 的学习
- 熟悉 Go 语言基础(goroutine, channel, sync.Mutex)
- 了解 RPC 的基本概念

## 工具和环境

> 请问你使用的开发环境是?
> - VSCode / GoLand?
> - 操作系统: Windows / macOS / Linux?
> - Go 版本是多少? (建议 1.13+)
>
> 根据你的环境,我会给出具体的配置建议。

## 任务拆解

### Step 1: 理解代码框架

```
src/mapreduce/
  |-- coordinator.go   # 调度器(你需要实现)
  |-- worker.go        # 工作节点(你需要实现)
  |-- rpc.go           # RPC 通信接口
  |-- common.go        # 共享数据结构
```

### Step 2: 实现 Coordinator

```go
// coordinator.go
type Coordinator struct {
    // TODO: 添加你认为需要的字段
    // 提示: 需要使用 sync.Mutex 保护并发访问
}

// 为什么需要锁?
// 多个 worker 同时向 coordinator 请求任务,
// 如果不对 state 加锁,会导致 race condition(竞态条件)。
```

### Step 3: 实现 Worker 循环

```go
// worker.go
func Worker(mapf func(string, string) []KeyValue,
            reducef func(string, []string) string) {

    for {
        reply := callGetTask()

        switch reply.TaskType {
        case MapTask:
            // 1. 读取输入文件
            // 2. 调用 mapf 处理数据
            // 3. 将中间结果写入临时文件
            // 4. 通知 coordinator 任务完成

        case ReduceTask:
            // 1. 读取中间文件
            // 2. 按 key 排序(why? 因为同一个 key 的数据才能一起处理)
            // 3. 调用 reducef 聚合
            // 4. 写入输出文件

        case WaitTask:
            time.Sleep(time.Second) // 无任务,等待

        case ExitTask:
            return // 所有任务完成,退出
        }
    }
}
```

### Step 4: 测试验证

```bash
# 运行测试(在 src/mapreduce 目录下)
go test -run TestBasic -v

# 应该看到类似输出:
# --- PASS: TestBasic (2.34s)
```

## 常见错误

| 症状 | 可能原因 | 解决方案 |
|------|----------|----------|
| `panic: runtime error: invalid memory address` | 空指针引用 | 检查 RPC reply 是否为 nil |
| 测试超时 | worker 死循环或死锁 | 检查锁的使用是否正确 |
| 某些文件内容为空 | map 输出未正确写入 | 检查文件创建和写入逻辑 |

## 面试准备

- **高频问题**: 解释你的 MapReduce 实现中如何保证容错?
- **思考题**: 如果 worker 在执行 map 任务时崩溃,你的 coordinator 如何处理?
- **进阶讨论**: exactly-once 语义在你的实现中如何体现? 有什么 trade-off?
- **系统设计**: 如果输入文件达到 TB 级别,你的架构需要做哪些调整?

---

*学习辅助材料 - 非官方课程材料*
```


