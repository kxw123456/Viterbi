# -*- coding: utf-8 -*-


def viterbi(obs, states, s_pro, t_pro, e_pro):
    """

    :param obs: 观测状态链
    :param states: 隐藏状态
    :param s_pro: 出现隐藏状态的概率
    :param t_pro: 状态转移概率
    :param e_pro: 发射概率（输出概率）
    :return: 最有可能的隐藏状态链
    """
    path = {s: [] for s in states}
    curr_pro = {}
    for s in states:
        curr_pro[s] = s_pro[s] * e_pro[s][obs[0]]
    for i in range(1, len(obs)):
        last_pro = curr_pro
        curr_pro = {}
        for curr_state in states:
            max_pro, last_sta = max(((last_pro[last_state] * t_pro[last_state][curr_state] * e_pro[curr_state][obs[i]],
                                      last_state) for last_state in states))
            curr_pro[curr_state] = max_pro
            path[curr_state].append(last_sta)

    max_pro = -1
    max_path = None
    for s in states:
        path[s].append(s)
        if curr_pro[s] > max_pro:
            max_path = path[s]
            max_pro = curr_pro[s]

    return max_path


if __name__ == '__main__':
    states = ('Healthy', 'Fever')
    observations = ('normal', 'cold', 'dizzy')
    start_probability = {'Healthy': 0.6, 'Fever': 0.4}
    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6},
    }
    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }
    obs = ['normal', 'cold', 'dizzy']
    print(viterbi(obs, states, start_probability, transition_probability, emission_probability))

    states = ('Rainy', 'Sunny')
    obs = ('walk', 'shop', 'clean')
    start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
    transition_probability = {
        'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
        'Sunny': {'Rainy': 0.4, 'Sunny': 0.6},
    }
    emission_probability = {
        'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
        'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
    }
    print(viterbi(obs, states, start_probability, transition_probability, emission_probability))