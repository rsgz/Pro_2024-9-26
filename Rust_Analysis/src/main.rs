#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::path::PathBuf;  // 拼接路径
use std::fs;  // 获取目录
// use std::io;
use std::collections::HashSet;  // 去重
// 写数据
use std::fs::OpenOptions;
use std::io::Write;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;
// 键值对
use std::collections::HashMap;

// 定义词性标签
#[derive(Debug, PartialEq, Clone)]
enum PosTag {
    Noun,         // 名词
    Verb,         // 动词
    Adjective,    // 形容词
    Adverb,       // 副词
    Preposition,  // 介词
    Determiner,   // 定冠词
    Article,      // 冠词
    Unknown,      // 未知
}


// 词汇表：将单词映射到词性标签
fn get_lexicon() -> std::collections::HashMap<String, PosTag> {
    let mut lexicon = std::collections::HashMap::new();
    lexicon.insert("新建".to_string(), PosTag::Verb);
    lexicon.insert("一个".to_string(), PosTag::Article);
    lexicon.insert("结构体".to_string(), PosTag::Noun);
    lexicon.insert("lazy".to_string(), PosTag::Adjective);
    lexicon.insert("on".to_string(), PosTag::Preposition);
    lexicon.insert("the".to_string(), PosTag::Determiner); // 现在添加了Determiner
    // 添加更多单词和标签...
    lexicon
}

// 分析句子并标记词性
fn pos_tag(sentence: &str) -> Vec<(String, PosTag)> {
    let lexicon = get_lexicon();
    let words: Vec<&str> = sentence.split_whitespace().collect();
    let mut tagged_words = Vec::new();

    for word in words {
        // 使用词汇表查找词性，如果没有找到，则标记为Unknown
        let tag = lexicon.get(word).cloned().unwrap_or(PosTag::Unknown); // 使用 cloned() 来克隆值
        tagged_words.push((word.to_string(), tag));
    }

    tagged_words
}

fn main() {
    let sentence = "新建 一个 结构体";
    let tagged_sentence = pos_tag(sentence);
    for (word, tag) in tagged_sentence {
        println!("{} - {:?}", word, tag);
    }
}