# Company Desc — 公司简短中文介绍库

> **维护策略**:**预填 + LLM 自动 enrich**(同 glossary.md 模式,宁滥勿缺)
>
> 每个 `.cnode` 在报告里 必须加 `data-desc="..."` 属性(从本文件取);
> 若标的不在本文件 → **LLM 必须先 append 到对应分类,再回报告使用**。
>
> **写作风格**:**30-60 字**,讲清"主营是什么 + 在产业链什么位置 + 关键标签"(可包含市占率 / 龙头地位 / 重要客户)。
> 避免营销词,要 verbal 中性。

---

## IP / EDA / 标准

- **ARM.US** = ARM Holdings,英国芯片 IP 授权龙头。设计 CPU/GPU/NPU 架构授权给 SoC 厂(高通/苹果/NVDA Grace 都基于 ARM)。每片 ARM-based SoC 必交版税。
- **CDNS.US** = Cadence Design Systems,EDA(芯片设计软件)双寡头之一。SoC/ASIC 设计必用,与 Synopsys 双寡头垄断。
- **SNPS.US** = Synopsys,EDA 另一寡头(与 Cadence 并列)。设计自动化工具 + IP 核库,所有先进制程 SoC 设计必用。

## 半导体 / 上游材料

- **STM.US** = STMicroelectronics,欧洲半导体综合龙头(法意合资)。SiC 功率器件全球 #1、MEMS 传感器领先,汽车+800V 电源大客户。
- **WOLF.US** = Wolfspeed,美国 SiC 衬底+器件龙头。150mm → 200mm 转产中,被重组后新管理层接手。
- **XFAB.PA** = X-FAB Silicon Foundries,欧洲半导体代工。美国 Commerce 点名的唯一高产能 SiC 代工,EU+US CHIPS Act 双背书。
- **ON.US** = onsemi,美国 SiC 综合 #2(STM 后)。自家 fab + Treo 800V 汽车平台。
- **IFX.DE** = Infineon Technologies,德国功率半导体龙头。SiC+GaN 综合,与 NVDA 联合开发 800V。
- **MPWR.US** = Monolithic Power Systems,美国高效 PMIC 电源管理芯片厂。AI 服务器+AI PC+机器人电源关键,跨多个 AI capex 主线。
- **MU.US** = Micron Technology,美国 LPDDR/HBM/NAND 三大件存储厂。LPDDR5X 美国独家,AI PC 主流内存。
- **TSM.US** = 台积电,全球最大芯片代工。InFO/SoIC/CoWoS 先进封装主导,2nm 制程领先 ASML。
- **NVDA.US** = NVIDIA,AI GPU 全球垄断(H100/Blackwell/Rubin)。Drive Thor 自动驾驶 + NIM/Jetson 物理 AI 平台。

## 半导体 / 上游设备

- **AEHR.US** = AEHR Test Systems,SiC 功率器件 burn-in 老化测试设备小盘龙头。跨光子学 + 800VDC 主题。
- **ASMPT.HK / 0522.HK** = ASMPT,先进封装设备(TCB 热压键合)龙头。CoWoS 等 2.5D/3D 封装核心装备。
- **ONTO.US** = Onto Innovation,先进封装/AI 衬底计量设备纯 play。所有封装产能扩张必用其测量设备。
- **AMAT.US** = Applied Materials,半导体设备综合大厂(沉积/刻蚀/CMP/计量)。市值~$1300亿。
- **AMKR.US** = Amkor Technology,全球封装代工 #2(ASE 之后)。CoWoS 等先进封装的核心合作伙伴。

## MLCC / 被动元件

- **300285.SHE** = 国瓷材料,A 股 MLCC 介质粉(钛酸钡)龙头。全球 #2,中国 80-90% 份额,三星电机第一供应商。
- **605376.SHG** = 博迁新材,纳米镍粉全球领跑(≤120nm)。MLCC 内电极材料,4 年长协。
- **4078.T** = Sakai Chemical,日本钛酸钡全球 #1(25-30% 份额),水热法工艺。
- **002859.SHE** = 洁美科技,MLCC 离型膜/载带国产替代领跑。纸质载带全球 #1。
- **KN.US** = Knowles Corporation,美股特种高可靠陶瓷电容(医疗/国防/半导设备用)。MLCC 高可靠细分。
- **VSH.US** = Vishay Intertechnology,最直接 AI-MLCC 受益的中游宽线供应商。
- **6981.T** = Murata Manufacturing,日本 MLCC 全球 #1。垂直整合自制材料+设备,成品龙头。
- **TTDKY.US** = TDK ADR,日本 TDK 公司 ADR。MLCC + HDD 磁头 + 电池 + InvenSense MEMS 综合。

## 半导体 / 中游器件

- **POWI.US** = Power Integrations,800V 链稳健的 AC-DC 集成芯片中游卖铲子。
- **NVTS.US** = Navitas Semiconductor,GaN 功率半导体小盘。NVDA 800V 链下游,但稀释/亏损红旗。
- **VICR.US** = Vicor Corporation,DC-DC 模块龙头。P/E 110,估值偏高的反面参照。
- **IPWR.US** = Ideal Power,B-TRAN 双向晶体管技术微盘。NVDA Rubin Ultra LOI 概念股。
- **AVGO.US** = Broadcom,半导体+软件综合。定制 ASIC(给 Google 做 TPU)龙头,市值 $2T+。
- **AMD.US** = Advanced Micro Devices,Ryzen CPU + MI300X AI 加速器。AMD AI PC Ryzen AI 300 主推。
- **INTC.US** = Intel,x86 CPU 巨头。Lunar Lake/Panther Lake 是 AI PC 主流 NPU SoC。
- **QCOM.US** = Qualcomm,Snapdragon 移动 SoC 龙头。Snapdragon X Elite/Plus 是 ARM 阵营 AI PC 旗舰。
- **MBLY.US** = Mobileye Global,Intel 拆分的 ADAS 芯片龙头。EyeQ ASIC 全球辅助驾驶 80% 市占。
- **AMBA.US** = Ambarella,边缘视觉 SoC 纯 play。机器人/自动驾驶/安防视觉芯片,跨多主题。
- **NXPI.US** = NXP Semiconductors,荷兰车规 MCU 全球 #1。汽车电子核心。
- **MXL.US** = MaxLinear,美国 Wi-Fi 7 + 连接芯片厂。
- **SIMO.US** = Silicon Motion,SSD 主控芯片龙头。本地 AI 推理需大 SSD,卖铲子。
- **SYNA.US** = Synaptics,触控芯片 + 边缘 AI。

## 物理 AI / 机器人零部件

- **603297.SHG** = 绿的谐波,A 股谐波减速器近垄断。全球第 3(Harmonic Drive、Nabtesco 之后),人形机器人关节核心。
- **603667.SHG** = 五洲新春,行星滚柱丝杠潜力股。Tesla Optimus 线性执行器核心零件,深度回调中启动。
- **603009.SHG** = 北特科技,行星滚柱丝杠双 player 之一。和五洲新春双押。
- **002338.SHE** = 奥普光电,A 股光电编码器领先纯 play。机器人关节角度精度的源头。
- **603728.SHG** = 鸣志电器,空心杯电机 A 股龙头。Maxon 风格,人形机器人手指等精细执行器。
- **688160.SHG** = 步科股份,无框力矩电机 + 伺服。人形机器人大型关节直驱。
- **6324.T** = Harmonic Drive Systems,日本谐波减速器全球龙头。人形机器人核心零件,1m+64% 已抛物线。
- **6268.T** = Nabtesco,日本 RV 减速器全球龙头。机器人本体大型关节。
- **6954.T** = Fanuc,日本工业机器人四大家族之一。
- **6506.T** = Yaskawa Electric,日本伺服+工业机器人本体。
- **RSW.LSE** = Renishaw,英国高精度编码器全球龙头。医疗 + 工业 + 航天多元业务。
- **002747.SHE** = 埃斯顿,A 股工业机器人本体龙头。
- **AVAV.US** = AeroVironment,美军 Switchblade 巡飞弹 + Puma 战术无人机主供。
- **KTOS.US** = Kratos Defense,XQ-58 协同战斗机 + 高超音速靶机。美军 NGAD/CCA 项目核心承包商。
- **002415.SHE** = 海康威视,全球安防监控/机器视觉龙头。Entity List 打压但产业地位未撼动。
- **002236.SHE** = 大华股份,全球安防 #2(海康之后)。
- **SYM.US** = Symbotic,仓储自动化龙头。Walmart $11B 长期合同。
- **AUTO.OL** = AutoStore,挪威仓储立体库自动化龙头。Ocado/Best Buy 客户。
- **CGNX.US** = Cognex Corporation,美国机器视觉龙头(工业精密检测)。
- **6861.T** = Keyence,日本机器视觉全球第二,毛利率 55% 业内最高。
- **ISRG.US** = Intuitive Surgical,da Vinci 手术机器人全球垄断。市值~$1500亿。
- **SYK.US** = Stryker,MAKO 骨科手术机器人 + 综合医疗器械。
- **DE.US** = Deere & Company,农业机械精准化龙头。See & Spray 智能耕作。

## 自动驾驶 / 车载

- **HSAI.US** = Hesai Group 禾赛科技,中国 LiDAR 出货全球第 1(车规+Robotaxi 双线)。中美关系打压下深度回调。
- **LAZR.US** = Luminar Technologies,美国 LiDAR(Velodyne 后合并体)。2026 已实质清盘($0.09)。
- **AEVA.US** = Aeva Inc,FMCW LiDAR 技术升级路线。
- **OUST.US** = Ouster,美国数字 LiDAR 厂(与 Velodyne 合并)。
- **603501.SHG** = 韦尔股份,A 股 CMOS 图像传感器(CIS)龙头,旗下 OmniVision 全球车规 CIS #3。深度回调中。
- **TRMB.US** = Trimble Inc,高精度 GNSS+测绘综合大厂。自动驾驶定位 + 农业 + 建筑多元业务。
- **AUR.US** = Aurora Innovation,美国自动驾驶卡车 L4 唯一上市纯 play。2025 Q4 Dallas-Houston 商业首单。
- **CRNC.US** = Cerence,车载语音 AI(Nuance 拆分)。

## AI 算力 / AI Agent

- **NBIS.US** = Nebius Group,GPU 算力出租新云。MSFT $17B 合同。
- **CRWV** = CoreWeave,GPU 算力出租另一玩家(IPO 后)。
- **IREN.US** = IREN Limited,GPU 算力 + 比特币挖矿混合。
- **CIFR.US** = Cipher Mining,Google $3B 合同的算力公司。
- **WULF.US** = TeraWulf,GPU 算力出租。
- **DDOG.US** = Datadog,云监控 + LLM observability 综合龙头。每个 Agent 部署都要监控。
- **MDB.US** = MongoDB,Atlas Vector 是企业 RAG 主流向量数据库。每个 RAG agent 必备。
- **NET.US** = Cloudflare,AI Gateway + Workers AI 边缘推理。
- **CFLT.US** = Confluent,Kafka 流式数据平台(Apache Kafka 商业版)。
- **SNOW.US** = Snowflake,数据仓库 + Cortex AI Agent 集成。
- **ESTC.US** = Elastic NV,Elasticsearch + vector search 搜索引擎。
- **FROG.US** = JFrog,软件供应链 + AI(Artifactory/Xray)。
- **FSLY.US** = Fastly,边缘计算 CDN(Cloudflare 竞争者),业务长期承压。
- **CRM.US** = Salesforce,CRM 全球龙头,2024 末发布 Agentforce(企业 Agent 平台)。
- **PLTR.US** = Palantir Technologies,政府+企业 AI 数据分析平台(Foundry + AIP)。
- **NOW.US** = ServiceNow,企业 IT 服务管理(ITSM)龙头,Now Assist 是其 Agent 产品。**⚠ 注 EODHD 数据曾异常**。
- **MNDY.US** = monday.com,以色列工作管理 SaaS(Asana 竞争者)。AI workflow agents 是新方向。
- **APPN.US** = Appian,美国低代码 BPM 平台。Process Automation + AI agents。
- **PATH.US** = UiPath,RPA(机器人流程自动化)龙头,2024-25 转型 Agentic Automation。
- **HUBS.US** = HubSpot,营销/销售 SaaS 中小企业市场。HubSpot AI 营销 agents。
- **NICE.US** = NICE Ltd,以色列客服自动化龙头。
- **ZS.US** = Zscaler,云安全网关。AI agents API 安全护栏新方向。
- **BILL.US** = BILL Holdings,美国 SMB 财务自动化 SaaS(应付应收 Bill Payment)。
- **AI.US** = C3.ai,企业 AI 应用平台(执行历史一般)。
- **GTLB.US** = GitLab,代码托管 + DevOps(GitLab Duo 是 AI 编程 agent)。
- **SOUN.US** = SoundHound AI,语音识别 + 语音 AI agents(微盘高波动)。
- **APP.US** = AppLovin,移动广告 AI 平台。
- **DBX.US** = Dropbox,云存储 + Dropbox AI 文档 agent。
- **S.US** = SentinelOne,AI 驱动的端点安全。
- **MSFT.US** = Microsoft,Azure 云 + Copilot Studio + OpenAI 战略合作。
- **GOOGL.US** = Alphabet,Google + Gemini LLM。
- **AMZN.US** = Amazon,AWS Bedrock Agents + 自营机器人(Kiva/Astro)。
- **META.US** = Meta Platforms,Llama 开源 LLM 持有方。
- **TSLA.US** = Tesla,FSD 自动驾驶 + Optimus 人形机器人。
- **LI.US / XPEV.US / NIO.US** = 理想/小鹏/蔚来,中国 EV 三新势力,L2+ 智能驾驶。
- **AAPL.US** = Apple,M 系列芯片 + Apple Neural Engine + 设备生态。

## 商业航天 / 防务

- **VNP.TO** = 5N Plus,西方少数能产锗/镓/铟 + AZUR 空间太阳能电池。中国出口管制下的关键供应商。
- **MTRN.US** = Materion Corporation,铍材料近垄断(空间反射镜/制导/高超音速)。
- **RKLB.US** = Rocket Lab,小型火箭发射 + 卫星总包。Serenity 持有过的 Evolution 标的。
- **RDW.US** = Redwire,空间太阳能阵(ROSA)+ 星敏感器。亏损 + 大额 ATM 稀释红旗。

## A 股半导体(韬定律)

- **688072.SHG** = 拓荆科技,混合键合/PECVD 设备。3D NAND 堆叠核心,韬定律直接依赖。
- **688120.SHG** = 华海清科,CMP 减薄设备国产近垄断。3D 堆叠必需。
- **688012.SHG** = 中微公司,刻蚀设备国产替代龙头。
- **002371.SHE** = 北方华创,半导体设备平台龙头(综合)。
- **600584.SHG** = 长电科技,先进封装代工 A 股龙头(全球前三)。
- **002156.SHE** = 通富微电,先进封装(给 AMD/华为代工)。

## 光子学(2026 历史种子)

- **AXTI.US** = AXT Inc,InP 衬底全球 40% 供应。光通信激光器链上游。
- **SIVE.ST** = Sivers Semiconductors,瑞典 SiPh 设计 + InP 收发器小盘。
- **LITE.US** = Lumentum Holdings,光通信器件龙头。进每个超大规模厂商 ASIC 的 BOM。
- **TSEM.US** = Tower Semiconductor,光子学界的台积电(IBM 收购完成后)。70% 产能锁到 2028。
- **SOI.PA** = Soitec,SOI 衬底 + CPO 衬底近垄断(法国)。
- **IQE.LSE** = IQE plc,化合物半导体外延片(英国)。Ge 供应商。

---

## 编辑日志

- **2026-06-02 创建**:初始预填 ~80 个跨 11 个主题的核心标的。每条 30-60 字中性描述,可被 .cnode 的 `data-desc` 引用。
- **维护**:每跑新主题,LLM 必须先 append 新标的 → 再用 `<div class="cnode" data-desc="...">` 引用。
