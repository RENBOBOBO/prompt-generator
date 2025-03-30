import os
import pandas as pd
from prompt_generator import PromptGenerator
from config import INPUT_FILE, OUTPUT_FILE
import logging

def analyze_reference_data(file_path: str):
    """分析参考数据中的提示词模式"""
    try:
        df = pd.read_csv(file_path)
        patterns = {
            'artistic': [],    # 艺术相关的表达
            'metaphor': [],    # 隐喻表达
            'scene': [],       # 场景描述
            'emotion': []      # 情感表达
        }
        
        for _, row in df.iterrows():
            if pd.notna(row['prompt_zh']) and pd.notna(row['prompt_en']):
                # 分析提示词模式
                # TODO: 实现模式分析逻辑
                pass
                
        return patterns
    except Exception as e:
        print(f"Error analyzing reference data: {str(e)}")
        return None

def main():
    """主程序入口"""
    try:
        # 检查输入文件是否存在
        if not os.path.exists(INPUT_FILE):
            raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")
            
        # 创建输出目录（如果不存在）
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        # 分析参考数据
        reference_patterns = analyze_reference_data('../参考数据.csv')
        if reference_patterns:
            print("Successfully analyzed reference patterns")
        
        # 初始化生成器
        generator = PromptGenerator()
        
        # 处理CSV文件
        generator.process_csv(INPUT_FILE, OUTPUT_FILE)
        
        print("处理完成！结果已保存到:", OUTPUT_FILE)
        
        # 评估结果
        df = pd.read_csv(OUTPUT_FILE)
        total_score = 0
        for _, row in df.iterrows():
            if pd.notna(row['prompt_zh']) and pd.notna(row['prompt_en']):
                scores = generator.evaluate_prompt(
                    row['prompt_zh'],
                    row['prompt_en'],
                    row['task']
                )
                total_score += sum(scores.values())
        
        print(f"Total evaluation score: {total_score}")
        
    except Exception as e:
        logging.error(f"程序运行出错: {str(e)}")
        print(f"程序运行出错: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main() 