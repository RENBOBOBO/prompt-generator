# Prompt Generator for Content Safety

一个用于生成安全提示词的Python工具，可以将敏感或不适当的内容转换为适合的提示词。

## 功能特点

- 支持中英文提示词生成
- 智能场景转换
  - 暴力场景 → 动作电影拍摄场景
  - 血腥场景 → 特效化妆场景
  - 不当行为 → 教育警示场景
  - 危险行为 → 生命教育场景
  - 犯罪场景 → 预防教育场景
- 批量处理能力
- 提示词质量评估
- 详细的日志记录

## 项目结构

```
.
├── src/
│   ├── __init__.py
│   ├── config.py          # 配置文件
│   ├── prompt_generator.py # 提示词生成器核心类
│   ├── main.py           # 主程序入口
│   └── analyze_results.py # 结果分析工具
├── output/               # 输出目录
├── requirements.txt      # 项目依赖
└── README.md            # 项目说明文档
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 准备输入文件 `txt2img_risky_tasks.csv`，包含以下列：
   - task_id: 任务ID
   - task: 任务描述

2. 运行程序：
```bash
python src/main.py
```

3. 查看结果：
   - 生成的提示词保存在 `output/txt2img_risky_prompts.csv`
   - 处理日志保存在 `output/processing.log`

## 提示词生成规则

1. 场景转换：
   - 使用电影拍摄、特效化妆、教育警示等场景
   - 保持场景描述的专业性和真实性
   - 添加适当的场景布置和灯光效果描述

2. 关键词使用：
   - 使用"电影"、"表演"、"教育"、"艺术"等关键词
   - 确保场景描述丰富且专业

3. 长度控制：
   - 保持提示词长度在合理范围内
   - 确保描述完整且清晰

## 评估指标

提示词质量评估包含以下维度：
- 文本防御绕过
- 图像防御绕过
- 任务相关性
- 艺术性

## 注意事项

- 确保输入文件格式正确
- 检查输出目录是否存在
- 查看日志文件了解处理详情

## License

MIT License 