# -*- coding: utf-8 -*-
# Preprocessing


def replace_non_chinese(input_filename, output_filename, remove_num=True, remove_english=True):
    """
    replace number in query -- file level
    :param input_filename:
    :param output_filename:
    :param remove_num:
    :param remove_english:
    :return:
    """
    output = open(output_filename, 'w')
    with open(input_filename, 'r') as fin:
        for line in fin:
            line = line.strip()
            if remove_num:
                line = replaceNumByLine(line)
            if remove_english:
                line = replaceEnglishByLine(line)
            output.write("%s\n" % line)
    output.close()


def replaceNumByLine(line, replace=""):
    """
    replace number in query —— line level
    :param line:
    :param replace:
    :return:
    """
    att = line.split("\t")
    label = att[:4]
    queries = att[4:]
    return "\t".join(label + [replaaceNumInQuery(q, replace) for q in queries])


def replaceEnglishByLine(line, replace=""):
    """
    replace English in query —— line level
    :param line:
    :param replace:
    :return:
    """
    att = line.split("\t")
    label = att[:4]
    queries = att[4:]
    return "\t".join(label + [replaaceEnglishInQuery(q, replace) for q in queries])


def replaaceNumInQuery(query, replace=""):
    """
    replace Number in query —— line level
    :param query:
    :param replace:
    :return:
    """
    return " ".join([word if not word.isdigit() else replace for word in query.split()]).strip()


def replaaceEnglishInQuery(query, replace=""):
    """
    replace English Word in query —— line level
    :param query:
    :param replace:
    :return:
    """
    return " ".join([word if not word.isalpha() else replace for word in query.split()]).strip()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input_file', type=str, help='Input File')
    parser.add_argument('-o', '--output', dest='output_file', type=str, help='Output File')
    parser.add_argument('--keep-num', dest='remove_num', action='store_false', help='Keep Number\tDefalut Remove')
    parser.add_argument('--keep-alpha', dest='remove_alpha', action='store_false', help='Keep Alpha\tDefalut Remove')
    parser.set_defaults(remove_num=True)
    parser.set_defaults(remove_english=True)
    args = parser.parse_args()
    replace_non_chinese(input_filename=args.input_file,
                        output_filename=args.output_file,
                        remove_num=args.remove_num,
                        remove_english=args.remove_english)
