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
| **Distributed Systems Core** | | | |
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
| **Raft-Specific** | | | |
| Term | 任期 | always | Raft中每次选举的编号，像总统的届数 |
| Log Entry | 日志条目 | always | Raft日志中的一条记录，包含命令和任期号 |
| Commit Index | 提交索引 | always | 已被多数节点确认、可以安全执行的日志位置 |
| Applied Index | 应用索引 | always | 已被状态机执行的最新日志位置 |
| Split Vote | 选票分裂 | always | 多个Candidate同时竞选，各自只拿到自己一票，无人胜出 |
| Election Timeout | 选举超时 | always | Follower等待Leader心跳的超时时间，超时后发起选举 |
| Heartbeat | 心跳 | always | Leader定期发给Follower的空AppendEntries，维持领导地位 |
| **Consistency Models** | | | |
| Linearizability | 线性一致性 | always | 所有操作按实时顺序原子执行，就像单机串行执行一样 |
| Serializability | 可串行化 | always | 多个并发事务的执行结果与某种串行执行结果相同 |
| Eventual Consistency | 最终一致性 | always | 如果没有新更新，所有副本最终会达到一致状态 |
| Causal Consistency | 因果一致性 | always | 有因果关系的操作必须按因果顺序被所有节点看到 |
| Snapshot Isolation | 快照隔离 | always | 每个事务看到的是某个时间点的数据快照，不受并发事务影响 |
| **Transaction & Concurrency** | | | |
| Two-Phase Commit (2PC) | 两阶段提交 | always | 分布式事务协议：先prepare询问所有参与者，再commit/abort |
| Two-Phase Locking (2PL) | 两阶段锁 | always | 事务分为加锁阶段和解锁阶段，保证可串行化 |
| Optimistic Concurrency Control (OCC) | 乐观并发控制 | always | 先执行后验证，冲突少时效率高 |
| MVCC | 多版本并发控制 | Multi-Version Concurrency Control | 每个写操作创建新版本，读操作读取旧版本，读写互不阻塞 |
| Blocking | 阻塞 | always | 事务因等待资源而暂停执行，无法继续推进 |
| Deadlock | 死锁 | always | 多个事务互相等待对方持有的资源，谁也无法继续 |
| Abort | 中止 | always | 事务执行失败，回滚所有已做的修改 |
| **Replication & Fault Tolerance** | | | |
| Primary-Backup | 主备复制 | always | 一个主副本处理请求，一个或多个备份副本同步数据 |
| State Machine Replication (SMR) | 状态机复制 | always | 所有副本以相同顺序执行相同命令，保证状态一致 |
| Split Brain | 脑裂 | always | 网络分区导致多个副本都认为自己是主节点，各自独立服务 |
| Failover | 故障切换 | always | 主节点故障后，备份节点接管服务的过程 |
| Fencing | 隔离栅 | always | 确保被判定为故障的节点不能再访问共享资源 |
| Lease | 租约 | always | 给主节点一个时间窗口的授权，超时后自动失效 |
| **Storage Systems** | | | |
| Chunk | 数据块 | always | 大文件被切分成固定大小的存储单元(如GFS的64MB) |
| Coordinator | 协调者 | always | 分布式系统中的中央控制节点，负责任务调度和元数据管理 |
| Metadata | 元数据 | always | 描述数据的数据，如文件名、大小、位置等 |
| Checksum | 校验和 | always | 数据完整性校验码，用于检测数据是否损坏 |
| Namespace | 命名空间 | always | 名称的层级组织方式，如文件系统的目录树 |
| **Security & Trust** | | | |
| Byzantine Fault | 拜占庭故障 | always | 节点不仅可能崩溃，还可能恶意行为或发送错误信息 |
| PBFT | 实用拜占庭容错 | Practical Byzantine Fault Tolerance | 容忍不超过1/3节点为拜占庭故障的共识协议 |
| Proof of Work (PoW) | 工作量证明 | always | 通过计算难题来证明付出了计算资源，用于比特币挖矿 |
| Cryptographic Hash | 密码学哈希 | always | 将任意数据映射为固定长度摘要的单向函数 |
| Digital Signature | 数字签名 | always | 用私钥签名、公钥验证，确保数据的来源和完整性 |
| Fork Consistency | 分支一致性 | always | 服务器可以隐藏更新造成分叉，但无法修复已产生的分叉 |
| 51% Attack | 51%攻击 | always | 攻击者控制超过半数算力，可以逆转区块链交易 |
| **Distributed Computing** | | | |
| Gossip | 八卦传播 | always | 节点间随机交换信息，最终全网一致 |
| Straggler | 掉队者 | always | 执行任务异常缓慢的节点，拖慢整体进度 |
| Data Locality | 数据局部性 | always | 将计算任务调度到数据所在的节点，减少网络传输 |
| Shuffle | 洗牌 | always | MapReduce中Map输出按key分组传输到Reduce节点的过程 |
| Barrier | 屏障 | always | 同步点，所有参与者到达后才能继续执行 |
| **Operating Systems** | | | |
| Kernel | 内核 | always | 操作系统的核心，管理CPU、内存、设备等底层资源 |
| Scheduler | 调度器 | always | 决定CPU下一个该运行哪个进程的组件，像老师安排谁先发言 |
| Mutex | 互斥锁 | always | 保证同一时间只有一个线程能访问共享资源的锁机制 |
| Semaphore | 信号量 | always | 控制多个线程访问有限资源的计数器，像厕所门口的指示灯 |
| Context Switch | 上下文切换 | always | CPU从执行一个进程切换到另一个进程时保存和恢复状态 |
| **Networking** | | | |
| TCP/IP | TCP/IP协议族 | always | 互联网的基础通信协议，TCP保证可靠传输，IP负责寻址路由 |
| UDP | UDP协议 | always | 无连接的传输协议，像发短信不保证对方收到，但速度快 |
| RPC | 远程过程调用 | Remote Procedure Call | 像调用本地函数一样调用远程服务器上的函数 |
| Throughput | 吞吐量 | always | 单位时间内系统能处理的请求量 |
| Latency | 延迟 | always | 从发出请求到收到响应的时间差 |
| **Programming / CS General** | | | |
| Algorithm | 算法 | always | 解决问题的步骤和方法，像菜谱指导你一步步做出菜 |
| Cache | 缓存 | always | 把常用数据存到快速存储中加速访问，像把常吃的放冰箱上层 |
| Concurrency | 并发 | always | 多个任务交替执行让用户感觉同时进行(单核也能做) |
| Parallelism | 并行 | always | 多个任务真正同时执行(需要多核CPU) |
| API | 应用程序接口 | Application Programming Interface | 软件组件之间约定的通信方式，像餐厅的菜单 |
| Transaction | 事务 | always | 一组操作要么全做要么全不做，像银行转账扣钱和加钱必须同时成功 |

## Part C: Web-Search Fallback for Unknown Terms

When a technical term is NOT in the glossary above:

1. **Search the term online** using web search: search `{term} distributed systems definition` or `{term} 分布式系统`
2. **Extract the Chinese translation** from the search results (typically from Chinese Wikipedia, CSDN, or official documentation)
3. **For first occurrence**: write the term with your best-effort Chinese explanation in parentheses
4. **Mark uncertain translations**: if you cannot find a reliable source, append `[注: 此术语翻译来自网络搜索，可能不准确]`

### Example

If the term `TrueTime` is not in the glossary:
```markdown
TrueTime(谷歌Spanner使用的时间同步服务，基于GPS和原子时钟，返回时间区间[earliest,latest])
```

### Priority for term sourcing

1. This glossary (Predefined terms)
2. Web search results (Chinese tech blogs, official docs, Wikipedia)
3. If no reliable source: best-effort explanation + uncertainty marker

---

## Part D: Quick Reference Patterns

**MapReduce 双风格示例:**

> 通俗版本: 就像开一家披萨店，顾客点100个披萨。你找10个厨师，每人做10个(映射)，然后把做好的披萨按口味摆到取餐台上(归约)。不需要知道哪个厨师做的，只看最终结果好不好。

> 专业化版本: MapReduce是一种分布式编程模型。Map阶段将输入数据拆分为独立分片并行处理，生成中间键值对；Reduce阶段将相同键的值聚合归约，输出最终结果。由Google在2004年论文中提出，核心思想是"分而治之"加"计算向数据移动"。

**CAP Theorem 双风格示例:**

> 通俗版本: 三个愿望只能选两个。你想让系统一直开放营业(可用性)、所有门店数据完全一致(一致性)、即使分店之间网络断了也能自治(分区容错)。现实是网络一定会断，所以分区容错必须选，剩下只能在一至性和可用性之间二选一。

> 专业化版本: CAP定理由Eric Brewer提出，指分布式系统中一致性(Consistency)、可用性(Availability)、分区容错性(Partition Tolerance)三者不可兼得。由于网络分区是必然发生的，实际是在CP和AP之间做权衡。CP系统(如ZooKeeper)牺牲可用性保证强一致；AP系统(如Cassandra)牺牲一致性保证始终可用。
