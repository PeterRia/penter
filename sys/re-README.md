正则表达式

正则表达式，又称规则表达式，通常用来检索、替换那些符合某个模式（规则）的文本。

1.原子

\w：用来匹配字母、数字、下划线；

\d：用来匹配数字；

\s：用来匹配空白字符；

\W、\D、\S用来匹配与\w、\d、\s相反的字符。

2、元字符

.：用来匹配任意字符；

^：用来匹配开始位置；

$：用来匹配结束位置；

*：表示重复0次及以上；

?：表示重复0次或一次；

+：表示重复一次及以上；

{3}：表示恰好出现3次；

{3，}：表示至少出现3次；

{4，7}：表示至少出现4次，至多出现7次；

t|s：表示出现t或者s；

[jsz]：表示出现j/s/z中的任意一个；

3.模式修正符

i：不区分大小写；

M：多行匹配；

U：根据unicode进行匹配；

S：让”.“也匹配换行符；

4.贪婪模式与懒惰模式

贪婪模式：尽可能多的匹配；

懒惰模式：尽可能少的匹配；
5.正则表达式函数

有re.match函数、re.search函数、全局匹配函数和re.sub函数。
全局匹配函数就要会找到所有符合规则的子字符串，而不像search函数只会匹配到第一个复合条件的。
re.compile(pat).findall(string)

pat指的是正则规则，string表示要查找的文本。

re.sub是个正则表达式方面的函数，用来实现通过正则表达式，实现比普通字符串的replace更加强大的替换功能。简单的替换功能可以使用replace()实现。