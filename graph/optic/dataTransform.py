import pandas as pd

NODE_TO_SITE = {}
SITE_TO_NODE = {}
NODE_TO_NEID = {}


def read_ne_site_info(topology_file, sheet_name="网元"):
    """
    input: topology_file , MDS导出的拓扑信息
    function: 读取topology文件， 建立网元和站点的对应关系
    """
    df = pd.read_excel(topology_file, sheet_name=sheet_name)
    # 使用第二行作为df的columns
    df.columns = df.values[0]
    df.drop(["序号"], inplace=True)

    for index, row in df.iterrows():
        ne_name = row["名称"]
        node_id = row["节点ID"]
        site_name = row["所属站点"]
        ne_info = {"node_id": node_id, "site": site_name}
        NODE_TO_SITE[ne_name] = ne_info

        if site_name in SITE_TO_NODE:
            SITE_TO_NODE[site_name].append({"ne": ne_name, "node_id": node_id})
        else:
            nodes = list()
            nodes.append({"ne": ne_name, "node_id": node_id})
            SITE_TO_NODE[site_name] = nodes

    print(NODE_TO_SITE)
    print(SITE_TO_NODE)


def read_ne_id_info(ne_file="ne.csv"):
    """
    :param 读取ASON导出的ne和ne id关系
    :return: 保存ne和ne_id关系
    """
    df = pd.read_csv(ne_file)

    for index, row in df.iterrows():
        node_id = row["NODE_ID"]
        ne_name = row["NET_NAME"]
        ip_address = row["NODE_ID_IPV4"]
        NODE_TO_NEID[ne_name] = {"node_id": node_id, "ip": ip_address}

    print(NODE_TO_NEID)


def match_site_neid():
    for key, value in NODE_TO_NEID.items():
        if key in NODE_TO_SITE:
            ne_info = NODE_TO_SITE[key]
            # 匹配逻辑待确认， site匹配多个node_id如何处理？
            print("match site: {}, node id: {}" % (ne_info["site"], value["NODE_ID"]))
        else:
            raise ValueError("node name {} unmatched" % key)


def replace_site_to_node_id(site_name, node_id):
    pass


if __name__ == "__main__":
    read_ne_site_info("test.xlsx")
    read_ne_id_info("ne.csv")
