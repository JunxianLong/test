# 常用命令

## 插入文档

1. 插入单条记录

```sql
db.test.insert({title: 'MongoDB 教程', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
})
```

ps：不指定`_id`字段

2. 插入多条记录

```sql
db.test.insertMany([{title: '多条插入_1', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
},{title: '多条插入_2', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
}])
```



## 查看文档

1. 查看test集合下所有文档

```sql
db.test.find()
```

2. 模糊查询

```sql
db.getCollection('test').find({"title":{$regex:/教程/}})
```

ps：

https://blog.csdn.net/u022812849/article/details/51314810

## 更新文档

1. update()方法

```sql
db.test.update(
{'title':'MongoDB 教程'},
{$set:{'title':'MongoDB'}}
)
```

```
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

**参数说明：**

- **query** : update的查询条件，类似sql update查询内where后面的。
- **update** : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
- **upsert** : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
- **multi** : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
- **writeConcern** :可选，抛出异常的级别。

2. save()方法

```sql
db.test.save(
{'_id':ObjectId('5eb6072612d2f32b14829e13'),
'title':'数据更新_1' ,
'description':'通过save()方法更新数据'}
)
```

# 标识说明

| 序号 |  标识  |   说明   |
| :--: | :----: | :------: |
|  1   | $regex | 模糊查询 |
|  2   |  $in   | 模糊查询 |
|  3   |  $gt   |   大于   |
|  4   |  $lt   |   小于   |
|  5   |  $gte  | 大于等于 |
|  6   |  $lte  | 小于等于 |

