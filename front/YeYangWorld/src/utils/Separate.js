function separate(text) {
    const lines = text.split('\n').filter(line => line.trim() !== ''); // 按换行符分割文本并过滤掉空白行
    const textPairs = [];

    for (let i = 0; i < lines.length; i += 2) {
        const englishLine = lines[i]; // 假设偶数行是英文
        const chineseLine = i + 1 < lines.length ? lines[i + 1] : ''; // 假设奇数行是中文，如果没有对应的中文行则留空
    
        textPairs.push({
            english: englishLine.trim(),
            chinese: chineseLine.trim()
        });
    }
    
    return textPairs;
  }

  export default separate;