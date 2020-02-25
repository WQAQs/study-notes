### **频率学派与贝叶斯学派**
贝叶斯学派与频率学派是当今数理统计的两大学派。对于样本分布$F(X,\theta)$,我们要对其中的未知$\theta$进行估计，让我们来看看频率学派（也称古典学派）和贝叶斯学派是如何做的：
-  **频率学派**
    （1）频率学派把需要推断的参数$\theta$看作是固定的未知常数，即对于一批样本，其分布$F(X,\theta)$是确定的，只不过$\theta$未知。同时，样本$X$是随机的。
    （2）频率学派从「自然」角度出发，试图直接为「事件」本身建模，即事件A在独立重复试验中发生的频率趋于极限p，那么这个极限就是该事件的概率。
- **贝叶斯学派**
    （1）贝叶斯学派否定了概率即频率的观点，贝叶斯学派并不从试图刻画「事件」本身，而从「观察者」角度出发。
    （2）贝叶斯学派引入了主观概率的概念，认为一个事件在发生之前，人们应该对它是有所认知的，即中的不是固定的，而是一个随机变量，并且服从分布，该分布称为**先验分布**（指抽样之前得到的分布），当得到样本$X$后，我们对的分布则有了新的认识，此时有了更新，这样就得到了**后验分布**（指抽样之后得到的分布）
    - **先验概率**：是根据以往经验和分析得到的概率。
    - **后验概率**：事情已经发生，求这件事发生是由某个原因引起的可能性的大小。
    - **条件概率公式**：事件A和事件B都是同一实验下不同的集合，一般事件A和事件B是有交集的，若没有交集，则条件概率为0
    $$
    P(A|B)=\frac{P(AB)}{P(B)}
    $$
    - **样本空间$\Omega$的一个划分**
    如果事件组$B_1,B_2,\cdots$满足:
    （1）$B_1,B_2,\cdots$两两互斥；
    （2）$B_1\cup B_2\cup\cdots =\Omega$;
    则称**事件组$B_1,B_2,\cdots$** 是 **样本空间$\Omega$的一个划分**。

    假设$B_1,B_2,\cdots$(相当于导致事件A发生的各种原因)是样本空间$\Omega$的一个划分，A为任一事件,则有**全概率公式**，**贝叶斯公式**如下：
    - **全概率公式**
    $$
    P(A)=\sum_{i=1}^{\infty}{P(B_i)P(A|B_i)}
    $$
    **理解**：全概率公式相当于把所可能出现事件A的情况基于不同的条件$B_i$进行累加。
    - **贝叶斯公式**
    贝叶斯公式是建立在条件概率的基础上寻找事件(即事件$A$)发生的原因（即$B_i$），即根据**先验分布$P(B)$**,结合观测结果（即样本数据，发生的事件A）,重新对各种原因概率得到新的认识，即**后验概率**：
    $$
    P(B_i|A)=\frac{P(B_i)P(A|B_i)}{\sum_{j=1}^{n}{P(B_j)P(A|B_j)}}
    $$

# markdown公式示例

  $$
  L(Y,f(X))=\begin{cases}
  1, Y\neq f(X)\\
  0, Y=f(X)
  \end{cases}
  $$

  $x \times y=z$

  $\int^{\infty}_{0}{xdx}$

  $\mathcal {ABCdefxyzXYZ123}$

  $\grave{a}$

  $\therefore$

  $$
  X^\mathrm T=
\left[
\begin{matrix}
 x_{11} & \cdots & x_{1N} \\
 \vdots & \ddots & \vdots \\
 x_{M1} & \cdots & x_{MN} \\
\end{matrix}
\right]
  $$

$\overbrace{a+b+c+d}^{2.0}$

  $$ \begin{aligned} L(w)&=\sum\limits^{N}{i=1}[y_i\log\pi(x_i)+(1-y_i)\log(1-\pi(x_i))]\&=\sum\limits^{N}{i=1}[y_i\log{\frac{\pi(x_i)}{1-\pi(x_i)}}+\log(1-\pi(x_i))]\&=\sum\limits^{N}_{i=1}[y_i(w\cdot x_i)-\log(1+\exp(w\cdot{x_i})] \end{aligned} $$

  $$
  \begin{aligned}
  M_1(x)=
  \begin{bmatrix}
  &a_{01}&a_{02}\\
  &0&0
  \end{bmatrix}
  &,M_2(x)=
  \begin{bmatrix}
  &b_{11}&b_{12}\\
  &b_{21}&b_{22}
  \end{bmatrix}
  \\
  M_3(x)=
  \begin{bmatrix}
  &c_{11}&c_{12}\\
  &c_{21}&c_{22}
  \end{bmatrix}
  &,M_4(x)=
  \begin{bmatrix}
  &1&0\\
  &1&0
  \end{bmatrix}
  \end{aligned}
  $$

  $$
{\underset {x\in S\subseteq X}{\operatorname {arg\,max} }}\,f(x):=\{x\mid x\in S\wedge \forall y\in S:f(y)\leq f(x)\}.
$$

$$
{\underset {x\in S\subseteq X}{\operatorname {max} }}\,f(x):=\{x\mid x\in S\wedge \forall y\in S:f(y)\leq f(x)\}.
$$

