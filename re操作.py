import redis


# conn = redis.Redis(host = "192.168.11.61", port = 6379)
#
# # 设置值
# conn.set("zhaoyun","赵云")
# #获取
# # val = conn.get("zhaoyun").decode("utf-8")
# #
# # nal = conn.get("qingqiu_name").decode("utf-8")
# #
#
#
#
# conn.hset("xx","k1","别改")
# conn.hset("xx","k2","就知道你会改")
#
# n = conn.hget("xx","k1").decode("utf-8")
#
# m = conn.hget("xx","k2").decode("utf-8")
#
#
# print(n,m)
# # print(val,nal)



conn = redis.Redis(host="192.168.11.148", port = 6379)

# conn.set("zy","赵云")
val = conn.get("zy").decode("utf8")
print(val)