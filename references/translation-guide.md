# CS English-Chinese Translation Guide (for Zero-Basis Learners)

## Part A: Translation Rules

1. **Terminology preservation**: Keep key CS terms in English. Translate only when the Chinese term is universally accepted in Chinese CS education (e.g., "consistency" → "一致性", "partition" → "分区").

2. **First occurrence**: Write `EnglishTerm(中文解释)` on first use. After that, use the English term only.

3. **Code handling**: Never translate code, variable names, function names, or CLI output. Translate comments only.

4. **Dual-style**: Provide both 通俗 (vulgarized/analogy-based) AND 专业化 (precise technical) explanations in the same output.

5. **Uncertainty marking**: When unsure about a translation, append `[注: 此部分翻译可能不准确]`.

6. **Zero-basis principle**: Never assume prior CS domain knowledge. Define every term on first use.

## Part B: CS Terminology Glossary

| English | 中文 | 何时保留英文 | 通俗解释 |
|---------|------|-------------|---------|
| **Distributed Systems** | | | |
| Raft | 筏式共识 | always | 像一船人投票选船长，多数同意才能做决定的一致性算法 |
| Paxos | 帕克索斯共识 | always | 比Raft更古老的共识协议，像多个议员投票通过法案 |
| MapReduce | 映射归约 | always | 把大任务拆成小任务分给多台电脑算(映射)，再汇总结果(归约) |
| GFS | 谷歌文件系统 | Google File System | 把一个大文件切成小块存在多台机器上的分布式存储系统 |
| Sharding | 分片 | always | 把数据切成碎片分散到不同数据库，像把书拆成章节放不同书架 |
| Consensus | 共识 | always | 多台机器就某个值达成一致意见的过程 |
| Replication | 复制 | always | 把数据拷贝多份存到不同机器，防止一台坏了就丢数据 |
| Partition | 分区 | always | 把系统分成多个独立部分，或把数据按规则切分存储 |
| Leader Election | 领导者选举 | always | 一群节点中选出一个主节点负责协调，像选班长 |
| Quorum | 法定多数 | always | 完成一个操作所需的最小同意节点数 |
| Fault Tolerance | 容错 | always | 部分组件故障时系统仍能正常工作的能力 |
| CAP Theorem | CAP定理 | 用英文缩写CAP | 分布式系统三者只能取二: 一致性(C)、可用性(A)、分区容错(P) |
| Vector Clock | 向量时钟 | always | 记录每台机器事件顺序的机制，像给每个事件盖时间戳 |
| Gossip Protocol | 八卦协议 | always | 节点间像传八卦一样互相传播信息，最终所有节点都知道 |
| ZooKeeper | 动物园管理员 | always | 分布式系统的协调服务，管理配置、命名、同步等元信息 |
| **Operating Systems** | | | |
| Kernel | 内核 | always | 操作系统的核心，管理CPU、内存、设备等底层资源 |
| Scheduler | 调度器 | always | 决定CPU下一个该运行哪个进程的组件，像老师安排谁先发言 |
| Mutex | 互斥锁 | always | 保证同一时间只有一个线程能访问共享资源的锁机制 |
| Semaphore | 信号量 | always | 控制多个线程访问有限资源的计数器，像厕所门口的指示灯 |
| Deadlock | 死锁 | always | 多个线程互相等待对方释放资源，谁也无法继续执行 |
| Virtual Memory | 虚拟内存 | always | 让程序以为自己有连续大内存，实际映射到物理内存+磁盘 |
| Page Fault | 缺页中断 | always | 程序访问的虚拟内存页不在物理内存中，需从磁盘加载 |
| Context Switch | 上下文切换 | always | CPU从执行一个进程切换到另一个进程时保存和恢复状态 |
| DMA | 直接内存访问 | Direct Memory Access | 设备不经过CPU直接把数据写入内存，解放CPU去做别的 |
| Interrupt | 中断 | always | 硬件通知CPU有紧急事情要处理，让CPU暂停当前工作 |
| Syscall | 系统调用 | always | 用户程序请求操作系统服务的接口，像找政府办事要填表 |
| **Networking** | | | |
| TCP/IP | TCP/IP协议族 | always | 互联网的基础通信协议，TCP保证可靠传输，IP负责寻址路由 |
| UDP | UDP协议 | always | 无连接的传输协议，像发短信不保证对方收到，但速度快 |
| HTTP | HTTP协议 | always | 浏览器和服务器之间的通信协议，网页用的就是这个 |
| DNS | 域名系统 | Domain Name System | 把人类易记的域名(google.com)转成机器用的IP地址 |
| Load Balancer | 负载均衡器 | always | 把请求分发到多台服务器，不让某一台太忙，像前台分配顾客 |
| CDN | 内容分发网络 | Content Delivery Network | 把内容缓存到离用户最近的服务器，加速访问速度 |
| NAT | 网络地址转换 | Network Address Translation | 让多台设备共享一个公网IP上网，像小区用一个门牌号收快递 |
| TLS/SSL | 传输层安全协议 | always | 加密网络通信防止窃听和篡改，网址锁头图标就是它 |
| RPC | 远程过程调用 | Remote Procedure Call | 像调用本地函数一样调用远程服务器上的函数 |
| Message Queue | 消息队列 | always | 把消息暂存起来让消费者异步处理，像快递暂存柜 |
| Throughput | 吞吐量 | always | 单位时间内系统能处理的请求量 |
| Latency | 延迟 | always | 从发出请求到收到响应的时间差 |
| **Databases** | | | |
| ACID | ACID特性 | 用英文缩写ACID | 事务的四个属性: 原子性、一致性、隔离性、持久性 |
| BASE | BASE特性 | 用英文缩写BASE | 牺牲强一致性换取可用性的分布式设计哲学 |
| Index | 索引 | always | 加速数据查询的数据结构，像书的目录页 |
| Transaction | 事务 | always | 一组操作要么全做要么全不做，像银行转账扣钱和加钱必须同时成功 |
| Replica | 副本 | always | 数据库数据的拷贝，用于容错或分担读请求 |
| Shard | 分片 | always | 数据库水平切分后的数据片段 |
| B-Tree | B树 | always | 数据库索引常用的一种平衡多路查找树结构 |
| LSM-Tree | LSM树 | Log-Structured Merge-Tree | 写优化型数据结构，把随机写变顺序写，NoSQL数据库常用 |
| **Programming / CS General** | | | |
| Algorithm | 算法 | always | 解决问题的步骤和方法，像菜谱指导你一步步做出菜 |
| Data Structure | 数据结构 | always | 组织和存储数据的方式，像衣柜、工具箱各有用途 |
| Recursion | 递归 | always | 函数调用自身来解决问题，像照镜子时镜子里还有镜子 |
| Cache | 缓存 | always | 把常用数据存到快速存储中加速访问，像把常吃的放冰箱上层 |
| Hash Table | 哈希表 | always | 通过键直接计算存储位置的数据结构，查找极快 |
| Queue | 队列 | always | 先进先出(FIFO)的数据结构，像排队买票 |
| Stack | 栈 | always | 后进先出(LIFO)的数据结构，像叠盘子 |
| Tree | 树 | always | 层次化数据结构，有根节点和子节点，像文件目录 |
| Graph | 图 | always | 由节点和边组成的网络结构，像地铁线路图 |
| Concurrency | 并发 | always | 多个任务交替执行让用户感觉同时进行(单核也能做) |
| Parallelism | 并行 | always | 多个任务真正同时执行(需要多核CPU) |
| Big O | 大O记法 | always | 描述算法效率随数据规模增长的增长率 |
| API | 应用程序接口 | Application Programming Interface | 软件组件之间约定的通信方式，像餐厅的菜单 |
| SDK | 软件开发工具包 | Software Development Kit | 开发某平台应用所需的工具集合，像乐高套装 |
| Framework | 框架 | always | 提供基础设施和约定让开发者填业务逻辑的半成品软件 |
| Middleware | 中间件 | always | 连接不同软件组件的中间层，像翻译官 |
| Container | 容器 | always | 轻量级虚拟化技术，打包应用及其依赖一起运行 |
| Virtualization | 虚拟化 | always | 把物理资源抽象成虚拟资源，一台物理机跑多个虚拟机 |
| Microservice | 微服务 | always | 把大应用拆成多个小服务独立部署和扩展的架构风格 |
| CI/CD | 持续集成/持续部署 | always | 自动化构建、测试和部署的软件开发实践 |
| Design Pattern | 设计模式 | always | 被反复验证的代码组织模板，像建筑的经典户型图 |
| Dependency Injection | 依赖注入 | always | 由外部传入依赖而非内部创建，降低耦合的设计技巧 |

## Part C: Quick Reference Patterns

**MapReduce 双风格示例:**

> 通俗版本: 就像开一家披萨店，顾客点100个披萨。你找10个厨师，每人做10个(映射)，然后把做好的披萨按口味摆到取餐台上(归约)。不需要知道哪个厨师做的，只看最终结果好不好。

> 专业化版本: MapReduce是一种分布式编程模型。Map阶段将输入数据拆分为独立分片并行处理，生成中间键值对；Reduce阶段将相同键的值聚合归约，输出最终结果。由Google在2004年论文中提出，核心思想是"分而治之"加"计算向数据移动"。

**CAP Theorem 双风格示例:**

> 通俗版本: 三个愿望只能选两个。你想让系统一直开放营业(可用性)、所有门店数据完全一致(一致性)、即使分店之间网络断了也能自治(分区容错)。现实是网络一定会断，所以分区容错必须选，剩下只能在一至性和可用性之间二选一。

> 专业化版本: CAP定理由Eric Brewer提出，指分布式系统中一致性(Consistency)、可用性(Availability)、分区容错性(Partition Tolerance)三者不可兼得。由于网络分区是必然发生的，实际是在CP和AP之间做权衡。CP系统(如ZooKeeper)牺牲可用性保证强一致；AP系统(如Cassandra)牺牲一致性保证始终可用。
