### 说明

##### zeng 2015论文结果，theano运行结果
> out/official_theano/
> test_pr_12_DEF_.txt max f1 0.3444444444445884, pre 0.396837349398, rec 0.304272517321

##### sentence+position的最好结果为"sentence_position/PCNN_ONE_DEF_6_PR.txt"
> out/sentence_position
> pytorch+CNN+sentence+position的结果
> PCNN_ONE_DEF_10_PR.txt max f1 0.3131628197126452, pre 0.340569877883, rec 0.289838337182

##### ">>> relation >>>"SDP的最好结果为"SDP_158/PCNN_ONE_DEF_6_PR.txt"
> out/SDP_62/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"单独编码）
> PCNN_ONE_DEF_7_PR.txt max f1 0.27240773286469777, pre 0.276456599287, rec 0.268475750577

> out/SDP_62_one/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"单独编码）
> PCNN_ONE_DEF_7_PR.txt max f1 0.2665966937811365, pre 0.244348244348, rec 0.293302540416

> out/SDP_158/
> pytorch+CNN+SDP在158设备上的运行结果（">>>"单独编码）
> PCNN_ONE_DEF_6_PR.txt max f1 0.27063073075815675, pre 0.26084627745, rec 0.281177829099

##### ">>>relation>>>"SDP的最好结果为"SDP_diff_relation_62_one/PCNN_ONE_DEF_6_PR.txt"
> out/SDP_diff_relation_62/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"与relation一起编码）
> PCNN_ONE_DEF_5_PR.txt max f1 0.2874743326487514, pre 0.292188431723, rec 0.282909930716

> out/SDP_diff_relation_62_one/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"与relation一起编码）
> PCNN_ONE_DEF_6_PR.txt max f1 0.3006097560976341, pre 0.318475452196, rec 0.284642032333

> out/SDP_diff_relation_62_two/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"与relation一起编码）
> PCNN_ONE_DEF_9_PR.txt max f1 0.29110512129374805, pre 0.273003033367, rec 0.311778290993

##### multi kernal SDP的最好结果为"SDP_diff_relation_multi_kernal_one/PCNN_ONE_DEF_5_PR.txt"
> out/SDP_diff_relation_multi_kernal/
> pytorch+CNN+SDP**(CNN具有大小不同的kernal)**在62设备上的运行结果（">>>"与relation一起编码）
> PCNN_ONE_DEF_8_PR.txt max f1 0.2841194529721782, pre 0.274986493787, rec 0.293879907621

> out/SDP_diff_relation_multi_kernal_one/
> pytorch+CNN+SDP**(CNN具有大小不同的kernal)**在62设备上的运行结果（">>>"与relation一起编码）
> PCNN_ONE_DEF_5_PR.txt max f1 0.2944499833830448, pre 0.346906812843, rec 0.255773672055

##### 只用sentence+CNN+MIL的最好结果为"sentence/PCNN_ONE_DEF_16_PR.txt"
> out/sentence/
> pytorch+CNN+sentence的结果（在原数据及模型的基础上，仅仅去除相对位置特征）
> PCNN_ONE_DEF_12_PR.txt max f1 0.08487746563060641, pre 0.087980173482, rec 0.0819861431871

merge_PCNN_result/PCNN_ONE_DEF_7_PR.txt max f1 0.34757834757834677, pre 0.384723195515, rec 0.316974595843
merge_PCNN_result_two/PCNN_ONE_DEF_6_PR.txt max f1 0.3613937711993956, pre 0.387822634017, rec 0.338337182448
merge_PCNN_result_one/PCNN_ONE_DEF_5_PR.txt max f1 0.32839290903848295, pre 0.330602691633, rec 0.326212471132
merge_PCNN_result_three/PCNN_ONE_DEF_8_PR.txt max f1 0.33645922136940126, pre 0.331281477336, rec 0.341801385681

merge_result/PCNN_ONE_DEF_6_PR.txt max f1 0.33504566210058806, pre 0.331264108352, rec 0.338914549654
merge_result_one/PCNN_ONE_DEF_7_PR.txt max f1 0.3577598216771699, pre 0.345718901454, rec 0.370669745958

sentence_position_PCNN/PCNN_ONE_DEF_6_PR.txt max f1 0.31599736668882594, pre 0.367534456355, rec 0.277136258661
