一、基于neo4j的kbqa

效果如图所示：

  ![avatar](/KBQA/movie/example.png)


主要流程：

数据准备-->问题抽象-->问题分类-->问题扩展-->答案生成

数据准备：
  
  mysql数据库中的genre（电影类型表）、movie（电影表）、movie_to_genre（电影-类型表）、person（演员表）、person_to_movie（演员-电影表）导出csv格式的数据
  通过load csv...  merge命令导入到neo4j图数据库中。
  
问题抽象：

  问题中涉及到专有的电影名称会转化为他的词性 nm。这样做的好处在于能让分类器减轻特征的选取工作量,也可以缩减训练集的规模。如（卧虎藏龙的评分是多少。抽象后的语句：nm的评分是多少）
  
问题分类：
  
  ![avatar](/KBQA/movie/classifier.png)
  
  通过分类查找对应模板句子和模板索引
  
问题扩展：

  将问题抽象中的实体词性替换成查询的实体内容（如：nm 评分  替换为 卧虎藏龙 评分）
  
答案生成：

  根据模板索引可以获取对应cypher语句
  
  根据实体内容可以填充cypher语句中参数


  
  
  
  
  
