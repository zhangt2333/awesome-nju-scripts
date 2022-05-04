#!/bin/bash
# written by zhangt2333

# how to use (demo like follows):
# bash njunet.sh
# bash njunet.sh -u 学号
# bash njunet.sh -u 学号 -p 密码
# bash njunet.sh logout

if [[ $@ == *"logout"* ]]; then
  curl http://p.nju.edu.cn/portal_io/logout -X GET
  exit 0
fi

njuId=""
password=""

paras=($@)
for ((i=0; i<$#; i++)); do
  if [[ ${paras[$i]} == "-u" ]] && [[ $i+1 -lt $# ]]; then
    njuId=${paras[$i+1]}
  fi

  if [[ ${paras[$i]} == "-p" ]] && [[ $i+1 -lt $# ]]; then
    password=${paras[$i+1]}
  fi
done

if [[ -z $njuId ]]; then
  echo "Enter NJU ID:"
  read njuId
fi

if [[ -z $password ]]; then
  echo "Enter password:"
  stty -echo
  read password
  stty echo
fi

curl http://p.nju.edu.cn/portal_io/login -X POST -d "username=$njuId&password=$password"
