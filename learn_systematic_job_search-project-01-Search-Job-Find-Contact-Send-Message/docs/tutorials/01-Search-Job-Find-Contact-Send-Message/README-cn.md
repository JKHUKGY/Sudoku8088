# AI 驱动的结构化求职

> 这节课教你用 AI 自动化求职中最关键的三个环节：**搜索岗位**、**找联系人**、**写个性化消息**。把机械重复的活交给 AI，你把精力放在真正重要的事情上——准备面试、提升技能、建立关系。

---

## 为什么要结构化投递？

先说一个现实：在 AI 时代，传统的"海投简历、坐等回复"已经越来越难奏效了。

根据 Revelio Labs 的数据，从 2023 年到 2025 年，美国入门级岗位的招聘量下降了约 35%。SignalFire 的研究发现，大型科技公司和成熟创业公司中，工作经验不足一年的新员工入职率下降了 50%。这不是危言耸听——AI 正在替代大量初级任务，企业发现留下一个 Senior 配上 AI，就能覆盖过去整个 Junior 团队的产出。

但这不是一篇贩卖焦虑的文章。恰恰相反，**AI 既是问题的来源，也是解决问题的工具**。

传统求职是一个漏斗：

- 投 100 份简历
- 可能只有 3-5 个回复
- 最后拿到 1 个 offer

问题出在哪里？**效率太低，命中率太低**。你把时间花在了大量的无效投递上，而不是精准出击。

结构化投递的思路完全不同：

- 用 AI 快速筛选出**真正匹配的岗位**
- 用 AI 找到岗位背后**可以联系的人**
- 用 AI 生成**个性化的联系消息**
- 然后**主动出击**——而不是被动等待

为什么主动联系这么重要？因为在没有职业积累的起步阶段，你的简历很可能被淹没在成千上万份申请中。但如果你能联系到内部的人——校友、团队成员、招聘官——你的简历被认真看的概率会提高 10 倍以上。

这就是本课程要教你的：**如何用 AI 让"主动出击"变得高效且有章可循**。

---

## 前置条件

这节课假设你已经完成了以下准备工作：

**你的定位已经想清楚了**

- 你知道自己想找什么方向的工作（Data Scientist？Software Engineer？Product Manager？）
- 你了解自己的优势和卖点
- 你的简历已经梳理好了

**你的个人资料已经整理好了**

我们在之前的课程中讲过如何用 AI 来梳理你的 profile 和 experience——把你的情况、你的目标、你的故事整理清楚。如果你还没做过这一步，建议先去完成那个课程。

**本课程的起点**是：你已经有了一份结构化的简历和清晰的求职目标。我们现在要做的是，**用 AI 把投递效率提升 10 倍**。

---

## 本课程的三个工具

这节课包含三个 AI Prompt 工具，它们形成一个完整的工作流：

**1. LinkedIn Job Search（搜索岗位）** — 需要 Claude for Chrome

- **输入**：你的简历、求职目标、筛选条件
- **做什么**：AI **操作你的浏览器**，在 LinkedIn 上浏览职位列表，点击每个职位查看完整 JD，根据你的条件进行匹配评分
- **输出**：一个结构化的 TSV 文件，包含匹配的岗位列表
- **为什么需要浏览器操作**：因为 AI 需要实际点击、滚动、读取页面内容

**2. LinkedIn Contact Finder（找联系人）** — 需要 Claude for Chrome

- **输入**：某个特定岗位的 JD + 你的简历
- **做什么**：AI **操作你的浏览器**，在公司 LinkedIn 页面上搜索四类人——Alumni（校友）、Future Peer（未来同事）、Recruiter（招聘官）、Hiring Manager（招聘经理）
- **输出**：一个结构化的 TSV 文件，包含可以联系的人和建议的联系理由
- **为什么需要浏览器操作**：因为 AI 需要在公司页面搜索、点击个人资料、读取信息

**3. LinkedIn Cold Message（写个性化消息）** — 任何 AI 都可以

- **输入**：某个特定联系人的信息 + 你的简历 + 你想要的切入点和目标
- **做什么**：AI 根据对方的背景和你的情况，生成个性化的 LinkedIn 消息
- **输出**：一条可以直接复制粘贴发送的消息
- **为什么不需要浏览器**：这一步只是文本生成，不需要操作网页

整个流程是这样的：

1. 先用 **Job Search** 找到一批匹配的岗位
2. 选择一个最想投的岗位，用 **Contact Finder** 找到可以联系的人
3. 选择一个联系人，用 **Cold Message** 生成个性化消息
4. 发送消息，建立联系，争取内推或面试机会

---

## 文件结构

在开始之前，先了解一下这个项目的文件结构：

```
project/
├── profile/                                    # 你需要准备的个人资料
│   ├── resume.md                               # 你的简历
│   ├── objective.md                            # 求职目标
│   ├── narrative.md                            # 补充说明（可选）
│   ├── job-search-additional-requirements.md   # 搜索时的额外要求
│   ├── job-description.md                      # 特定岗位的 JD（用于工具 2 和 3）
│   ├── code-message-target-person.md           # 联系目标（用于工具 3）
│   ├── code-message-out-reach-key.md           # 联系切入点（用于工具 3）
│   └── code-message-outcome.md                 # 期望结果（用于工具 3）
│
├── docs/                                          # Prompt 模板和生成的 Prompt
│   ├── linkedin-job-search-prompt.template.md     # 工具 1 的模板
│   ├── linkedin-job-search-prompt.md              # 生成的 Prompt
│   ├── linkedin-job-search-results.tsv            # 示例：搜索结果
│   ├── linkedin-contact-finder-prompt.template.md # 工具 2 的模板
│   ├── linkedin-contact-finder-prompt.md          # 生成的 Prompt
│   ├── contacts.md                                # 示例：联系人列表
│   ├── linkedin-cold-message-prompt.template.md   # 工具 3 的模板
│   └── linkedin-cold-message-prompt.md            # 生成的 Prompt
│
├── prompt_generator.py        # 核心脚本：将模板和你的资料合并生成 Prompt
└── mise.toml                  # 快捷命令配置
```

**关键理解**：

- `*.template.md` 是**模板文件**，里面有占位符（如 `{{RESUME_CONTENT}}`）
- `prompt_generator.py` 脚本会读取你在 `profile/` 目录下准备的文件，填充到模板中
- 生成的 `*.md` 文件（不带 template）就是你要发给 AI 的完整 Prompt

---

## 运行环境

这个项目只需要一个全局的 Python 环境，不需要创建虚拟环境。

**安装依赖**：

```bash
# 如果你已经有 mise，直接运行
mise install

# 或者确保你有 Python 3.12+
python --version
```

**可用的快捷命令**：

```bash
mise run gen-job-search      # 生成 Job Search Prompt
mise run gen-contact-finder  # 生成 Contact Finder Prompt
mise run gen-cold-message    # 生成 Cold Message Prompt
```

你也可以直接运行 Python 脚本：

```bash
python prompt_generator.py job-search
python prompt_generator.py contact-finder
python prompt_generator.py cold-message
```

---

## 工具 1: LinkedIn Job Search

### 这个工具做什么

当你有了简历和求职目标后，第一步是找到匹配的岗位。传统的做法是自己在 LinkedIn 上一个个翻看——但这太慢了，而且容易遗漏好机会。

这个工具让 AI 替你做这件事：

1. AI 在 LinkedIn 搜索页面浏览职位列表
2. **点击每个职位**查看完整的 JD（不是只看标题）
3. 根据你的简历和目标进行**匹配评分**
4. 输出一个**结构化的 TSV 文件**，按匹配度排序

### 你需要准备什么

在 `profile/` 目录下准备以下文件：

**[profile/resume.md](./profile/resume.md)** - 你的简历

这是最重要的输入。AI 会用你的简历来判断哪些岗位适合你。格式示例可以看我们提供的示例文件。

**[profile/objective.md](./profile/objective.md)** - 求职目标

告诉 AI 你在找什么样的工作。示例：

```markdown
- Objective: Find a full time job in Data Scientist, Machine Learning Engineer
- Current Situation: Master's graduate, Feb 2026
- Visa Status: F1, need H1B Sponsor
- Location Preference: Remote or NYC/Boston
- Salary Expectation: $80k+
```

**[profile/narrative.md](./profile/narrative.md)** - 补充说明（可选）

如果有一些难以在简历中体现的软性偏好，可以写在这里。比如："喜欢小团队"、"看重 work-life balance"等。

**[profile/job-search-additional-requirements.md](./profile/job-search-additional-requirements.md)** - 额外的筛选要求

比如：

```markdown
- Output limit: 15 positions
- Only include jobs posted within the last 7 days
- Exclude contract/temporary positions
- Focus on positions that sponsor H1B
```

### 如何生成 Prompt

准备好上述文件后，运行：

```bash
mise run gen-job-search
```

这个命令会调用 [prompt_generator.py](./prompt_generator.py)，它做的事情很简单：

1. 读取模板文件 [docs/linkedin-job-search-prompt.template.md](./docs/linkedin-job-search-prompt.template.md)
2. 读取你在 `profile/` 下准备的文件
3. 把模板中的占位符（如 `{{RESUME_CONTENT}}`）替换成你的实际内容
4. 输出到 [docs/linkedin-job-search-prompt.md](./docs/linkedin-job-search-prompt.md)

如果你想了解具体的替换逻辑，可以直接阅读 [prompt_generator.py](./prompt_generator.py) 的源码——代码很简单，就是字符串替换。

### 如何使用生成的 Prompt

**重要**：这一步必须使用 **Claude for Chrome**（或其他能操作浏览器的 AI）。普通的 ChatGPT 或 Claude 网页版做不了这件事，因为它们无法操作你的浏览器。

1. 在 Chrome 浏览器中打开 LinkedIn Jobs 搜索页面，确保你已经登录
2. 输入你想要的职位关键词（如 "Data Scientist"）
3. 打开 Claude for Chrome，将生成的 [docs/linkedin-job-search-prompt.md](./docs/linkedin-job-search-prompt.md) 的内容粘贴给它
4. AI 会自动操作你的浏览器：点击职位、滚动页面、读取 JD、分析匹配度
5. 最后 AI 会输出一个 TSV 文件

### 输出结果

AI 会生成一个 TSV 文件，类似这样：

[docs/linkedin-job-search-results.tsv](./docs/linkedin-job-search-results.tsv)

每一行包含：

- `title` - 职位名称
- `company` - 公司名称
- `location` - 地点
- `posting_date` - 发布时间
- `short_description` - 简短描述
- `reasoning` - **为什么这个岗位适合你**（这是关键！）
- `job_link` - 职位链接

**重要建议**：虽然 AI 帮你整理了这个列表，但我**强烈建议**你自己开一个 Excel 或 Google Sheets 来跟踪每个岗位——你投递了没有？什么时候投的？有没有收到回复？有没有需要跟进的？

这部分属于**手动管理**的工作，不在本课程的范围内。本课程专注于用 AI 自动化搜索和筛选，但最终的跟踪和管理还是需要你自己来做。

---

## 工具 2: LinkedIn Contact Finder

### 这个工具做什么

找到匹配的岗位后，下一步是找到这个岗位背后可以联系的人。

很多人投简历就是直接点 "Apply"——但这样你的简历会被淹没在几百上千份申请中。更聪明的做法是**找到内部的人**，让他们帮你内推或者至少让招聘官更认真地看你的简历。

这个工具帮你找四类人：

**Alumni（校友）** - 回复率 40-60%

这是最容易建立联系的人。同校情谊是天然的信任基础，他们往往愿意花几分钟帮一个学弟学妹。

**Future Peer（未来同事）** - 回复率 30-50%

和你申请的职位类似的人。他们能告诉你团队的真实情况、面试流程、文化氛围。

**Recruiter（招聘官）** - 回复率 20-40%

直接负责招聘的人。如果你能和他们建立联系，你的简历会被更认真地对待。

**Hiring Manager（招聘经理）** - 回复率 5-15%

最难联系但价值最高的人。如果他们回复了，基本就是面试的入场券。

### 你需要准备什么

**[profile/job-description.md](./profile/job-description.md)** - 目标岗位的 JD

从 Job Search 结果中选择一个你最想投的岗位，把完整的 JD 复制到这个文件里。我们提供了一个 Nasdaq Data Scientist 的示例。

**[profile/resume.md](./profile/resume.md)** - 你的简历

AI 会从你的简历中提取你的学校信息，用来搜索校友。

### 如何生成 Prompt

```bash
mise run gen-contact-finder
```

生成的 Prompt 在 [docs/linkedin-contact-finder-prompt.md](./docs/linkedin-contact-finder-prompt.md)。

### 如何使用

**重要**：这一步同样必须使用 **Claude for Chrome**。AI 需要在你已登录的 LinkedIn 上操作浏览器来搜索联系人。

1. 在 Chrome 浏览器中打开目标公司的 LinkedIn 页面（如 `linkedin.com/company/nasdaq`），确保你已经登录
2. 打开 Claude for Chrome，将生成的 Prompt 内容粘贴给它
3. AI 会自动操作你的浏览器：在公司页面搜索、点击"People"标签、筛选联系人、点击个人资料查看详情
4. 最后输出一个联系人列表

### 输出结果

AI 会生成一个类似这样的结果：

[docs/contacts.md](./docs/contacts.md)

每个联系人包含：

- `category` - 类别（Alumni/Future Peer/Recruiter/Hiring Manager）
- `name` - 姓名
- `title` - 职位
- `school_match` - 校友关系（如果有）
- `connection_degree` - 连接度（2nd 还是 3rd）
- `recent_activity` - 最近活动
- `linkedin_url` - 个人主页链接
- `outreach_angle` - **建议的联系切入点**

AI 还会给你一个**联系优先级建议**——先联系谁、为什么。

---

## 工具 3: LinkedIn Cold Message

### 这个工具做什么

找到联系人后，最后一步是写一条能让对方愿意回复的消息。

这不是一件容易的事。大部分人的 cold message 是这样的：

> "Hi, I'm a recent graduate looking for a job. I saw you work at [Company]. Would you be willing to refer me?"

这种消息的问题是：**太泛了**。对方每天可能收到几十条这样的消息，为什么要回复你？

好的 cold message 需要做到：

1. **个性化** - 让对方知道你是专门联系他/她的，不是群发
2. **有价值** - 给对方一个回复你的理由
3. **低门槛** - 不要一上来就要求太多

这个工具帮你生成符合这些原则的消息。

### 你需要准备什么

**[profile/code-message-target-person.md](./profile/code-message-target-person.md)** - 联系目标

从 Contact Finder 的结果中选一行，直接复制粘贴到这个文件里。

**[profile/code-message-out-reach-key.md](./profile/code-message-out-reach-key.md)** - 联系切入点

你为什么要联系这个人？有什么共同点或者能引起对方兴趣的东西？

从下面选一个最适合你的情况，或者根据实际情况修改：

- `We're both [School] alumni, I saw she's in the [team] I'm applying to` — 校友角度
- `I read his/her post about [topic] and have thoughts to share` — 回应对方的动态
- `I built a similar project to what they're working on, have a live demo: [URL]` — 展示你的作品
- `I wrote a paper on the same topic they specialize in` — 学术/专业共鸣
- `We have [N] mutual connections` — 共同人脉

如果你不确定用什么切入点，可以留空——AI 会根据对方的信息帮你建议几个选项。

**[profile/code-message-outcome.md](./profile/code-message-outcome.md)** - 期望结果

你希望这次联系达成什么？从下面选一个：

- `Get a 15-minute phone call to learn about the team` — **推荐**，最低门槛，最高回复率
- `Ask for a referral to the open position` — 比较直接，适合已经有一定联系的情况
- `Request a coffee chat to understand the company culture` — 建立关系，不急于求成
- `Get advice on breaking into this field` — 请教模式，让对方感到被尊重

**建议**：如果是第一次联系，选第一个或第三个。"15 分钟电话"或"coffee chat"门槛最低，对方最容易答应。等建立了关系之后，再请求 referral。

### 如何生成 Prompt

```bash
mise run gen-cold-message
```

生成的 Prompt 在 [docs/linkedin-cold-message-prompt.md](./docs/linkedin-cold-message-prompt.md)。

### 如何使用

**好消息**：这一步不需要 Claude for Chrome。你可以用**任何 AI**——ChatGPT、Claude 网页版、Claude Code、都可以。因为这一步只是文本生成，不需要操作浏览器。

把生成的 Prompt 粘贴给任何你喜欢的 AI，它会帮你生成个性化的消息。

### 输出结果

AI 会生成可以直接复制粘贴的消息，类似这样：

[profile/code-message.md](./profile/code-message.md)

```
Hi Rachel, I saw your post about the Boston tech team! I'm a Math MS at NYU
with a background in ETL and ML. I built a predictive project similar to
Nasdaq's market data needs (demo: https://demo.example). Would you be open
to a referral or a brief chat about the Graduate DS role?
```

AI 还会解释为什么这样写——开头用了什么 hook、为什么选择这个 value proposition、为什么这个 ask 是合适的。

---

## 完整工作流示例

我们用 Nasdaq Data Scientist 岗位作为例子，演示整个流程。

### 第 1 步：搜索岗位（使用 Claude for Chrome）

准备好 `profile/` 目录下的文件后：

```bash
mise run gen-job-search
```

打开 LinkedIn Jobs 搜索页面，登录你的账号，然后打开 **Claude for Chrome**，把生成的 Prompt 粘贴给它。AI 会操作你的浏览器执行搜索。

结果示例：[docs/linkedin-job-search-results.tsv](./docs/linkedin-job-search-results.tsv)

在这个示例中，AI 找到了 15 个匹配的岗位，第一个就是 Nasdaq 的 Data Scientist - Graduate 职位。

### 第 2 步：选择 Nasdaq，找联系人（使用 Claude for Chrome）

把 Nasdaq 的 JD 复制到 [profile/job-description.md](./profile/job-description.md)，然后：

```bash
mise run gen-contact-finder
```

打开 Nasdaq 的 LinkedIn 公司页面（`linkedin.com/company/nasdaq`），然后用 **Claude for Chrome** 执行生成的 Prompt。

结果示例：[docs/contacts.md](./docs/contacts.md)

AI 找到了：

- 4 个 Alumni（包括一个 NYU 校友 Sagar，是 2nd degree connection）
- 3 个 Future Peer
- 3 个 Recruiter（包括 Rachel，Campus Recruiting Lead）
- 3 个 Hiring Manager

### 第 3 步：选择一个联系人，写消息（任何 AI 都可以）

根据 AI 的建议，我们先联系 Rachel（Campus Recruiting Lead）——因为她是 2nd degree，而且一个月前发过关于 Boston tech interns 的帖子，说明她正在积极招人。

准备好联系人信息和切入点后：

```bash
mise run gen-cold-message
```

这一步不需要 Claude for Chrome，你可以用任何 AI（ChatGPT、Claude 网页版等）来生成消息。

结果示例：[profile/code-message.md](./profile/code-message.md)

### 第 4 步：发送消息

直接复制生成的消息，在 LinkedIn 上发送。

然后等待回复。如果 5-7 天没有回复，可以发一条简短的 follow-up。如果还是没有回复，就换下一个联系人。

---

## 保存你的结果

我建议你把 AI 生成的所有结果——TSV 文件、联系人列表、消息——都保存到这个 repo 里。

好处：

1. **有记录可查**：你可以回顾自己联系过哪些人、发过什么消息
2. **方便迭代**：如果某个消息效果好，可以作为模板复用
3. **形成系统**：求职是一个持续的过程，有系统比没系统强太多

---

## 常见问题

### 为什么 Alumni 回复率最高？

这是人类心理：

- **内群体偏好**：同校 = 自己人，天然有信任基础
- **利他动机**：很多人在职业起步时被校友帮助过，想 pay it forward
- **低成本**：回复一条消息只需要 2 分钟，如果能帮到一个学弟学妹，何乐而不为

### 消息应该多长？

LinkedIn Connection Request 有 **300 字符**的限制，所以你的消息必须精简。

原则：**越短越好**。如果能用 3 句话说清楚，就别用 5 句。

### 多久应该 follow up？

- 第一次联系后 **5-7 天**
- 最多 follow up **2 次**
- 如果还是没有回复，就 move on，联系下一个人

### 被拒绝了怎么办？

大部分情况下，对方不会明确拒绝你——他们只是不回复。这很正常。

记住：

- Alumni 回复率 40-60%——这意味着每 10 个人，有 4-6 个会回复
- 你只需要 1-2 个回复就够了
- 不要把"不回复"当成"拒绝"，对方可能只是忙

---

## 导师寄语

为什么要学这个？

求职是大多数人职业生涯中最焦虑的时刻之一。你投了几十份简历，没有回音；你参加了招聘会，递出去的简历石沉大海；你开始怀疑自己是不是不够好。

但问题可能不在你——问题在方法。

传统的求职方法是为信息匮乏的时代设计的：那时候，能找到招聘信息就是一种竞争力。但现在，信息泛滥，人人都能在 LinkedIn 上找到几百个"看起来不错"的岗位。竞争的战场已经转移了——**不是谁能找到机会，而是谁能让机会看到自己**。

这就是为什么"主动联系"变得如此重要。你不再是一个被动等待筛选的申请者，而是一个主动建立联系的职业人。这个思维转变，比任何具体技巧都重要。

AI 在这里扮演的角色是什么？它是你的加速器。它不能替你建立关系——那仍然需要你亲自去做。但它可以帮你省下几十个小时的机械工作：浏览职位、搜索联系人、起草消息。把这些时间省下来，你可以花在更重要的事情上：准备面试、提升技能、和联系人进行真正的对话。

最后说一句：**求职是一个技能，而技能是可以练习的**。第一次写 cold message 可能很别扭，第五次就会顺很多。第一次被忽略可能很沮丧，第十次就会坦然了。

你正在学习的，不只是几个 AI 工具的用法——而是一种**在 AI 时代主动出击**的思维方式。这个思维方式会陪伴你整个职业生涯。

祝你好运。

---

## 快速参考

**生成 Prompt 的命令**：

```bash
mise run gen-job-search      # 工具 1: 搜索岗位
mise run gen-contact-finder  # 工具 2: 找联系人
mise run gen-cold-message    # 工具 3: 写消息
```

**关键文件**：

- [profile/resume.md](./profile/resume.md) - 你的简历
- [profile/objective.md](./profile/objective.md) - 求职目标
- [profile/job-description.md](./profile/job-description.md) - 目标岗位 JD
- [prompt_generator.py](./prompt_generator.py) - 核心脚本

**示例输出**：

- [docs/linkedin-job-search-results.tsv](./docs/linkedin-job-search-results.tsv) - 搜索结果示例
- [docs/contacts.md](./docs/contacts.md) - 联系人列表示例
- [profile/code-message.md](./profile/code-message.md) - 消息示例
