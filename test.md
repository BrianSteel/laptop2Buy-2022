
$
\displaystyle
P_\Theta(G;C) = \prod_{e \in E} p(e \in E) \times \prod_{e \not \in E} p(e \not \in E)
\\[5px]
% = P_\Theta(G;C) 
= \prod_{e \in E} \frac {e^{\Phi(e)}} {1 + e^{\Phi(e)}} \times \prod_{e \not \in E} \frac {1} {1 + e^{\Phi(e)}}
\\[5px]
% = \log P_\Theta(G;C) 
= \log( \frac {e^{\Phi(e_0)}} {1 + e^{\Phi(e_0)}} \times \frac {1} {1 + e^{\Phi(e_0)}} \times \frac {e^{\Phi(e_1)}} {1 + e^{\Phi(e_1)}} \times \frac {1} {1 + e^{\Phi(e_1)}} \times ....)
\\[8px]
% = \> \> \> \log( \frac {e^{\Phi(e_0)}} {1 + e^{\Phi(e_0)}} \times \frac {1} {1 + e^{\Phi(e_0)}} \times ....)
\\[8px]
= \> \> \> \log( \frac {e^{\Phi(e_0)}} {1 + e^{\Phi(e_0)}}) + log(\frac {1} {1 + e^{\Phi(e_0)}}) \times ....
\\[8px]
= \> \> \> \log e^{\Phi(e_0)} - log(1 + e^{\Phi(e_0)}) + log\,1 - log(1 + e^{\Phi(e_0)}) \times ....
\\[8px]
% = \> \> \> \Phi(e_0) - log(1 + e^{\Phi(e_0)}) - log(1 + e^{\Phi(e_0)}) \times ....
\\[8px]
= \> \> \> \sum_{e \in E} \Phi(e_0) - \sum_{e \in E} \,log(1 + e^{\Phi(e)}) - \sum_{e \not \in E} \,log(1 + e^{\Phi(e)})  
\\[8px]
% \because \> \> \> \log P_\Theta(G;C) = l_\Theta(G;C) \> - \>
% \\[12px]
% \implies l_\Theta(G;C) = \sum_{e \in E} \Phi(e) - \sum_{e \in E} 2\,log(1 + e^{\Phi(e)})
% \\[5px]
% \implies l_\Theta(G;C) = \sum_{e \in E} \Phi(e) - \sum_{e \in  V \times V} \log(1 + e^{\Phi(e)})
l_\Theta(G;C) = \sum_{e \in E} \Phi(e) - \sum_{e \in  V \times V} \log(1 + e^{\Phi(e)})   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \,\,eq(3)
% \begin{pmatrix}1 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0\end{pmatrix}
$ 