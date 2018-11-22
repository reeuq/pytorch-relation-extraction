### 说明

##### zeng 2015论文结果，theano运行结果
> out/official_theano/

##### sentence+position的最好结果为"sentence_position/PCNN_ONE_DEF_6_PR.txt"
> out/sentence_position
> pytorch+CNN+sentence+position的结果

##### ">>> relation >>>"SDP的最好结果为"SDP_158/PCNN_ONE_DEF_6_PR.txt"
> out/SDP_62/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"单独编码）
>
> out/SDP_62_one/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"单独编码）
>
> out/SDP_158/
> pytorch+CNN+SDP在158设备上的运行结果（">>>"单独编码）

##### ">>>relation>>>"SDP的最好结果为"SDP_diff_relation_62_one/PCNN_ONE_DEF_6_PR.txt"
> out/SDP_diff_relation_62/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"与relation一起编码）
>
> out/SDP_diff_relation_62_one/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"与relation一起编码）
> 
> out/SDP_diff_relation_62_two/
> pytorch+CNN+SDP在62设备上的运行结果（">>>"与relation一起编码）

##### multi kernal SDP的最好结果为"SDP_diff_relation_multi_kernal_one/PCNN_ONE_DEF_5_PR.txt"
> out/SDP_diff_relation_multi_kernal/
> pytorch+CNN+SDP**(CNN具有大小不同的kernal)**在62设备上的运行结果（">>>"与relation一起编码）
>
> out/SDP_diff_relation_multi_kernal_one/
> pytorch+CNN+SDP**(CNN具有大小不同的kernal)**在62设备上的运行结果（">>>"与relation一起编码）
