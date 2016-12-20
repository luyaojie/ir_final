# -*- coding: utf-8 -*-
# Preprocessing


def replace_non_chinese(input_filename, output_filename, remove_num=True, remove_alpha=True, remove_url=True):
    """
    replace number in query -- file level
    :param input_filename:
    :param output_filename:
    :param remove_num:
    :param remove_alpha:
    :param remove_url:
    :return:
    """
    output = open(output_filename, 'w')
    with open(input_filename, 'r') as fin:
        for line in fin:
            line = line.strip()
            if remove_num:
                line = replaceNumByLine(line)
            if remove_alpha:
                line = replaceEnglishByLine(line)
            if remove_url:
                line = replaceUrlByLine(line)
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
    return "\t".join(label + [replaceNumInQuery(q, replace) for q in queries])


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
    return "\t".join(label + [replaceEnglishInQuery(q, replace) for q in queries])


def replaceUrlByLine(line, extract=True):
    """
    replace English in query —— line level
    :param line:
    :param extract:
    :return:
    """
    att = line.split("\t")
    label = att[:4]
    queries = att[4:]
    return "\t".join(label + [replaceUrlInQuery(q, extract) for q in queries])


def replaceNumInQuery(query, replace=""):
    """
    replace Number in query —— line level
    :param query:
    :param replace:
    :return:
    """
    return " ".join([word if not word.isdigit() else replace for word in query.split()]).strip()


def replaceEnglishInQuery(query, replace=""):
    """
    replace English Word in query —— line level
    :param query:
    :param replace:
    :return:
    """
    return " ".join([word if not word.isalpha() else replace for word in query.split()]).strip()


def replaceUrlInQuery(query, extract=True):
    """
    extract url in query
    :param query:
    :param extract:
    :return:
    """
    if is_url(query) and extract:
        return extract_url_keyword(query)
    return query


def is_url(query):
    """
    judge a query whether url or not
    :param query:
    :return:
    """
    if query.startswith("http") or query.startswith("www"):
        return True
    else:
        return False


def extract_url_keyword(url):
    """
    Extract Url Keyword
    :param url:
    :return:
    """
    url = url.replace(" ", "")
    if "http://" in url:
        url = url.replace("http://", "")
    if "https://" in url:
        url = url.replace("https://", "")
    if "www." in url:
        url = url.split("www.")[1]
    if "/" in url:
        url = url.split("/")[0]
    return url.replace(".", "_")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input_file', type=str, help='Input File')
    parser.add_argument('-o', '--output', dest='output_file', type=str, help='Output File')
    parser.add_argument('--keep-num', dest='remove_num', action='store_false', help='Keep Number\tDefalut Remove')
    parser.add_argument('--keep-alpha', dest='remove_alpha', action='store_false', help='Keep Alpha\tDefalut Remove')
    parser.add_argument('--keep-url', dest='remove_url', action='store_false', help='Keep URL\tDefalut Remove')
    parser.set_defaults(remove_num=True)
    parser.set_defaults(remove_alpha=True)
    parser.set_defaults(remove_url=True)
    args = parser.parse_args()
    replace_non_chinese(input_filename=args.input_file,
                        output_filename=args.output_file,
                        remove_num=args.remove_num,
                        remove_alpha=args.remove_alpha)
