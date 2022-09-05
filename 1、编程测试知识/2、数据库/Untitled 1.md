entity实体

attribute属性

relationship联系

primary key主键

foreign key外键

rule规则

project投影

join连接

divide除

union并

intersection交

difference差

insert增加

update更新

delete删除

create创建

table表

drop删除

alter修改

view视图

index索引

primary file主要数据文件

transaction log事务日志文件

null空

check约束

column列

add添加

values值

constraint约束

count统计记录个数

sum总和

avg平局值

max最大值

min最小值

distinct去除重复

where=,,条件

having=,,条件

group by分组

compute by显示详细记录

unique唯一约束

unique index唯一索引

clustered index聚集索引

nonclustered index非聚集索引

with encryption加密

default默认

begin....end语句块

select @a=10赋值语句（可同时对多个变量赋值）

set @a=10赋值语句

break跳出循环

continue结束本次循环，开始下一条语句

procedure存储过程

restore还原

backup备份

 

下列是一些数据库中经常碰到的英文单词：

Access method（访问方法）：此步骤包括从文件中存储和检索记录。

Alias（别名）：某属性的另一个名字。在SQL中，可以用别名替换表名。

Alternate keys（备用键，ER/关系模型）：在实体/表中没有被选为主健的候选键。

Anomalies（异常）参见更新异常（update anomalies）

Application design（应用程序设计）：数据库应用程序生命周期的一个阶段，包括设计用户界面以及使用和处理数据库的应用程序。

Attribute（属性）（关系模型）：属性是关系中命名的列。

Attribute（属性）（ER模型）：实体或关系中的一个性质。

Attribute inheritance（属性继承）：子类成员可以拥有其特有的属性，并且继承那些与超类有关的属性的过程。

Base table（基本表）：一个命名的表，其记录物理的存储在数据库中。

Binary relationship（二元关系）：一个ER术语，用于描述两个实体间的关系。例如，panch Has Staff。

Bottom-up approach（自底向上方法）：用于数据库设计，一种设计方法学，他从标识每个设计组建开始，然后将这些组件聚合成一个大的单元。在数据库设计中，可以从表示属性开始底层设计，然后

将这些属性组合在一起构成代表实体和关系的表。

Business rules（业务规则）：由用户或数据库的管理者指定的附加规则。

Candidate key（候选键，ER关系模型）：仅包含唯一标识实体所必须得最小数量的属性/列的超键。

Cardinality（基数）：描述每个参与实体的可能的关系数目。

Centralized approach（集中化方法,用于数据库设计）：将每个用户试图的需求合并成新数据库应用程序的一个需求集合

Chasm trap（深坑陷阱）：假设实体间存在一根，但某些实体间不存在通路。

Client（客户端）：向一个或多个服务器请求服务的软件应用程序。

Clustering field（群集字段）：记录总的任何用于群集（集合）航记录的非键字段，这些行在这个字段上有相同的值。

Clustering index（群集索引）：在文件的群集字段上定义的索引。一个文件最多有一个主索引或一个群集索引。

Column（列）：参加属性（attribute）。

Complex relationship（复杂关系）：度数大于2的关系。

Composite attribute（复合属性）：由多个简单组件组成的属性。

Composite key（复合键）：包含多个列的主健。

Concurrency control（并发控制）：在多用户环境下同时执行多个十五并保证数据完整性的一个DBMS服务。

Constraint（约束）：数据库不允许包含错误数据的一致性规则。

Data conversion and loading（数据转换和加载）：数据库应用生命周期重的一个阶段，包括转换现有数据到新数据库中以及酱下耨应用程序转换到新的数据库上运行。

Data dictionary（数据字典）：参见系统目录（system catalog）。

Data independence（数据独立性）：使用数据的应用程序的数据描述部分。这意味着，如果将新的数据结构添加到数据库中，或者数据库中现有的结构被修改了，那么使用此数据库的就会受到影响，除

非应用程序不直接依赖于被修改的部分。

Data model（数据模型）：描述数据、数据间关系以及数据的约束的概念的一个集成的集合。

Data redundancy（数据冗余）：参见冗余数据（redundant data）。

Data security（数据安全）：包括对数据库对象（如表和视图）的访问和使用以及用户可以在这些对象上实施的操作。

Database（数据库）：是逻辑上相关的数据（以及这些数据的描述）的一个共享的集合，用于解决公司对信息的需求。

Database design（数据库设计）：数据库应用生命周期中的一个阶段，包括创建一个支持公司的操作和目标的数据库的设计。

Database integrity（数据库完整性）：指存储数据的正确定和一致性。完整性通常用约束来表达。

Database Management System，DBMS（数据库管理系统）：一个能够让用户定义、创建和维护数据库并控制对数据库的访问的软件系统。

Database planning（数据库规划）：能尽可能有效的实现数据库应用的各阶段的管理活动。

Database server（数据库服务器）：同服务器。

DBMS engine（DBMS引擎）：同服务器。

DBMS selection（DBMS选择）：数据库应用生命周期中的一个阶段，包括选择一个合适的DBMS来支持数据库应用。

Degree of a relationship（关系的度）：一个关系中参与的实体的个数。

Denormalization（反规范化）：形式上，这个术语指的是对基本表结构的修改，这样新的表比原始的表的规范化程度要低。但也可以用此属于更宽泛地形容将两个表和并成一个新表的情形，而这个新表

与原来的表具有相同的范式，但比原表包含更多的空值。

Derived attribute（派生属性）：表示其值可以从一个相关属性和属性集的值派生得到的属性，这个属性在实体中不是必须的。

Design methodology（设计方法学）：一种结构化的方法，它使用过程、工具和文档来支持和简化设计过程。

Disjoint constraint（无连接约束）：描述子类的成员间的关系，并指明超类某个成员是否有可能成为一个或多个子类的成员。

Domain（域）：一个或多个属性的取值范围。

Entity（实体）：具有相同性质的对象的集合，它是由用户或公司标识并可独立存在的。

Entity integrity（实体完整性）：在一个基本表中，主健列的值不能为空。

Entity occurrence（实体出现）：实体中的一个唯一可标识的对象。

Entity-Relationship model（实体关系模型）：公司的实体、属性和关系的详细逻辑表示。

Fact-finding（事实发现）：使用诸如面谈和提问等技术收集关于系统的事实、需求和性能的形式化过程。

Fan trap（扇形陷阱）：但从第三个实体扇出的两个实体有1:*关系时出现扇形陷阱，但这两个实体在他们之间应该有直接关系以提供必要的信息

Field（字段）：同元组（Tuple）。

File（文件）：存储在副主存储器中的相关记录的一个命名集合。

File-based system（基于文件的系统）：一个文件集合，用来管理（创建、插入、删除、更新和检索）一个或多个文件中的数据，并产生基于这些文件中的数据的应用（通常是报表）。

File organization（文件组织）：当文件存储在磁盘上时，对文件中的记录的安排方式。

First normal form（1NF，第一范式）：表中的每个列的交叉处以及记录包含切进包含一个值的表。

Foreign key（外健）：一个表中的一个列或者多个列的集合，这些列匹配某些其他（也可能是同一个）表中的候选键。

4GL, Fourth-Generation Language（第四代语言）：一种非过程化语言，比如SQL，他只需要用户定义必须完成什么操作，4GL负责将所进行的操作翻译成如何实现这些操作。

Full functional dependency（完全函数依赖）：一个列在功能上依赖于复合主健，但不依赖于主健的任何一个子集的条件。

Functional dependency（函数依赖）：描述表中列之间的关系。

Generalization（泛化）：通过标识实体间的公共特征使实体间差别最小化的过程。

Generalization hierarchy（泛化层次结构）：同类型层次（type hierarchy）。

Global data model（全局数据模型）：代表整个公司（和被模型化的公司的一部分）的数据模型。

Implementation（实现）：数据库应用生命周期中的一个阶段，包括数据库和应用程序设计的物理实现。

Index（索引）：一种允许DBMS将特定的记录更快的放置到文件中，从而加快对用户查询的响应的数据结构。

Infomation system（信息系统）：能够在整个公司范围内收集、管理、控制和分发数据/信息的资源。

Inheritance（继承）：参见属性继承（attribute inheritance）。

Integrity constaints（完整性约束）：防止出现数据库中的数据不一致的约束。

IS-A hierarchy（IS－A层次结构）：同类型层次结构（type hierarchy）。

Local logical data model（局部逻辑数据模型）：代表特定用户视图或用户视图的组合的数据模型。

Logical database design（逻辑数据库设计）：基于特定的数据模型构建公司的数据的模型的过程，但不依赖于特定的DBMS以及其他的物理条件。

Meta-data（元数据）：关于数据的数据，参见系统目录（system catalog）。

Mision objective（使命目标）：标识数据库必须支持的特定任务。

Mission statement（使命语句）：定义数据库应用程序的主要目标。

Multiplicity（多样性）：定义与某个相关实体的一次出现有关的实体的出现数目。

Multi-valued attribute（多值属性）：为一个实体的出现保存多个值的属性。

Nonkey attribute/column（非键属性/列）：不是键的一部分的属性/列。

Normal forms（范式）：规范化过程的一个阶段。前三个范式分别为第一范式（1NF）、第二范式（2NF）、第三范式（3NF）。

Normalization（规范化）：一种产生带有需要的特性的技术，这种特性能支持用户和公司的需求。
