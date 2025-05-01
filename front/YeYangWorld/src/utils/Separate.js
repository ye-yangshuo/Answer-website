function separate(text) {
    const lines = text.split('\n').filter(line => line.trim() !== ''); // 按换行符分割文本并过滤掉空白行
    let englishText = '';
    let chineseText = '';

    lines.forEach((line, index) => {
      if (index % 2 === 0) {
        chineseText += line + '\n'; // 偶数行为中文
      } else {
        englishText += line + '\n'; // 奇数行为英文
      }
    });
  
    // 移除最后一个多余的换行符
    englishText = englishText.trim();
    chineseText = chineseText.trim();
    return [englishText,chineseText];
  }

  export default separate;