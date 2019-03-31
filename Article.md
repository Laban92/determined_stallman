Gasp uses machine learning to predict respiratory rate using only a pulse oxymetry data and heart rate. Tracking respiratory rate usually includes strapping electrodes onto a person's chest and monitoring chest movement, but Gasp enables us to monitor someone's respiratory rate using tiny sensors (PPG, heart rate monitors) which can easily be fitted to any smart watch or fitness band.
Respiratory rate is predicted using Gradient Boosted Decision Trees  for each millisecond being within 5 milliseconds from the annotated breath intake. Knowing respiratory rate along with the oxygen saturation changes, we can estimate the absorbtion of oxygen by the body (if oxygen saturation drops quickly after breath intake, it indicates that the oxygen is being used in metabolizing calories). The change in blood oxygenation is linearly related to respiratory quotient used in Weir formula for calculating calorie expenditure within 99% certainty.

![alt text](https://user-images.githubusercontent.com/32731048/55285284-e2f6e600-5388-11e9-8af8-f273edbdbea8.jpg)

Gasp allows us to monitor change in oxygen intake volume (VO₂) by monitoring respiration rate change, as well as oxygenation level change rate between breaths (SpO2).

Furthermore, there have been some significant interest in sleep tracking in the last couple of years, with Huawei teaming up with Harvard  Medical School to develop state of the art sleep tracking algorithms for it's smart devices. Gasp promises to surpass these algorithms since respiration rate has been shown to be one of the best sleep phase indicators.