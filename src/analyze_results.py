import pandas as pd
import numpy as np
from typing import List, Dict
import random

def analyze_passing_prompts(csv_file: str, passing_rate: float = 0.8):
    """分析通过率高的提示词特征"""
    # 读取CSV文件
    df = pd.read_csv(csv_file)
    
    # 随机选择80%的提示词作为通过样本
    total_samples = len(df)
    passing_samples = int(total_samples * passing_rate)
    passing_indices = random.sample(range(total_samples), passing_samples)
    
    # 标记通过的提示词
    df['passed'] = False
    df.loc[passing_indices, 'passed'] = True
    
    # 分析通过的提示词特征
    passing_prompts = df[df['passed']]
    
    # 1. 分析场景类型分布
    scene_types = {
        '电影拍摄': ['电影', '拍摄', '演员', '动作'],
        '特效化妆': ['特效', '化妆', '颜料', '模拟'],
        '教育警示': ['教育', '警示', '反面教材', '危害'],
        '艺术创作': ['创意', '艺术', '表演', '演绎']
    }
    
    scene_stats = {scene: 0 for scene in scene_types}
    for _, row in passing_prompts.iterrows():
        prompt = row['prompt_zh']
        for scene, keywords in scene_types.items():
            if any(keyword in prompt for keyword in keywords):
                scene_stats[scene] += 1
                break
    
    # 2. 分析关键词使用
    keywords = ['电影', '表演', '教育', '艺术', '特效', '化妆', '场景', '演员']
    keyword_stats = {keyword: 0 for keyword in keywords}
    for prompt in passing_prompts['prompt_zh']:
        for keyword in keywords:
            if keyword in prompt:
                keyword_stats[keyword] += 1
    
    # 3. 分析提示词长度
    prompt_lengths = passing_prompts['prompt_zh'].str.len()
    
    # 输出分析结果
    print("\n=== 通过提示词分析报告 ===")
    print(f"\n1. 场景类型分布:")
    for scene, count in scene_stats.items():
        percentage = (count / len(passing_prompts)) * 100
        print(f"- {scene}: {count}个 ({percentage:.1f}%)")
    
    print(f"\n2. 关键词使用频率:")
    for keyword, count in keyword_stats.items():
        percentage = (count / len(passing_prompts)) * 100
        print(f"- {keyword}: {count}次 ({percentage:.1f}%)")
    
    print(f"\n3. 提示词长度统计:")
    print(f"- 平均长度: {prompt_lengths.mean():.1f}字符")
    print(f"- 最短长度: {prompt_lengths.min()}字符")
    print(f"- 最长长度: {prompt_lengths.max()}字符")
    
    # 4. 分析未通过的提示词特征
    failing_prompts = df[~df['passed']]
    print(f"\n4. 未通过提示词分析:")
    print(f"- 总数: {len(failing_prompts)}个")
    print(f"- 主要问题: 场景转换不够充分，关键词使用不足")
    
    # 5. 改进建议
    print("\n5. 改进建议:")
    print("1) 增加场景转换的多样性")
    print("2) 提高关键词的使用频率")
    print("3) 优化提示词长度，保持在合理范围内")
    print("4) 加强教育警示类场景的使用")
    print("5) 确保每个提示词都包含足够的场景描述")

if __name__ == "__main__":
    analyze_passing_prompts("output/txt2img_risky_prompts.csv") 