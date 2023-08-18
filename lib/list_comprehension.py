#!/usr/bin/env python3


def return_evens(num_list):
    list = [i for i in num_list if i % 2 == 0]

    return list


def make_exclamation(sentence_list):
    list_of_sentences = [sentences + "!" for sentences in sentence_list]

    return list_of_sentences

