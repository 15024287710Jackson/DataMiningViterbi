import pandas as pd
import math

def read_file(file):
    document = open(file)
    record_lines= []
    while 1:
        each_line = document.readline()
        each_line = each_line.strip('\n')
        if not each_line:
            break
        # print(para)
        record_lines.append(each_line)
    document.close()
    return record_lines

def Viterbit(squence,all_states,element,prior,state_change,type_pro):
    # print(squence)
    print('all_states:',all_states)
    print('element:',element)
    print('prior:', prior)
    print('state_change:', state_change)
    print('type_pro:', type_pro)

    chain = {state:[] for state in all_states}
    now_probability={}
    for everystate in all_states:
        now_probability[everystate]=math.log(prior[everystate])+math.log(type_pro[everystate][str(squence[0]).upper()])
    for num in range(1,len(squence)):
        previous_pro= now_probability
        now_probability={}
        for now_state in all_states:
            add_pro_all={}
            for pre_state in all_states:
                pre = previous_pro[pre_state]
                tran_state=math.log(state_change[pre_state][now_state])
                now_pro=math.log(type_pro[now_state][str(squence[num]).upper()])
                add_pro=pre+tran_state+now_pro
                add_pro_all[pre_state]=add_pro
            # max_probability, pre_sta=max(previous_pro[pre_state]+ math.log(state_change[pre_state][now_state]) + math.log(type_pro[now_state][str(squence[0]).upper()]) for pre_state in all_states)
            biggest = max(zip(add_pro_all.values(), add_pro_all.keys()))
            now_probability[now_state] = biggest[0]#max
            chain[now_state].append(biggest[1])#存入上一次来自哪个链的
    print(now_probability)
    max_zip = max(zip(now_probability.values(), now_probability.keys()))
    max_pro = max_zip[0]  # max
    print(max_pro)
    max_final_label=max_zip[1]
    final_chain=chain[max_final_label]
    return final_chain

def output(final_chain):
    last_sign=1
    for count in range(1,len(final_chain)):
        if(final_chain[count] != final_chain[count-1]):
            print(last_sign,' ',count,' state ',final_chain[count-1])
            last_sign=count

if __name__ == '__main__':
    hmm_param=read_file("example.hmm")
    examplefa = read_file("example.fa")
    del examplefa[0]
    line_one=hmm_param[0].split(" ")
    num_state=line_one[0]
    num_element=line_one[1]
    element=list(line_one[2])#'A','C','G','T'
    line_two = hmm_param[1].split(" ")
    A_prior=float(line_two[0])
    B_prior = float(line_two[1])
    prior={}
    prior['A'] = A_prior;
    prior['B'] = B_prior;
    line_three = hmm_param[2].split(" ")
    while '' in line_three:
        line_three.remove('')
    AtoA=float(line_three[0])
    AtoB = float(line_three[1])
    A_1=float(line_three[2])
    A_2 = float(line_three[3])
    A_3 = float(line_three[4])
    A_4 = float(line_three[5])
    line_four = hmm_param[3].split(" ")
    while '' in line_four:
        line_four.remove('')
    BtoA=float(line_four[0])
    BtoB = float(line_four[1])
    B_1=float(line_four[2])
    B_2 = float(line_four[3])
    B_3 = float(line_four[4])
    B_4 = float(line_four[5])
    sequence=''
    for each_sam in examplefa:
        sequence=sequence+each_sam;
    # print(sequence)
    A_fourpro=[A_1,A_2,A_3,A_4]
    B_fourpro=[B_1,B_2,B_3,B_4]
    all_states={'A','B'}
    state_change={}
    type_pro={}
    for state in all_states:
        state_change[state]={}
        type_pro[state] = {}
    state_change['A']['A'] = AtoA
    state_change['A']['B'] = AtoB
    state_change['B']['A'] = BtoA
    state_change['B']['B'] = BtoB
    # print(state_change)
    for each_state in all_states:
        i=0
        for ele in element:
            if(each_state=='A'):
                type_pro[each_state][ele] = A_fourpro[i]
                i=i+1
            else:
                type_pro[each_state][ele] = B_fourpro[i]
                i = i + 1
    final_chain=Viterbit(sequence, all_states, element,prior, state_change, type_pro)
    output(final_chain)
    # print(final_chain[0:300])
    print(sequence[0])
    print(sequence[1])
    print(sequence[2])
    print(sequence[3])