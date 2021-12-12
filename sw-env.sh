#/bin/bash
# Jesko Mueller (c) 2021
# ZHAW CCP1-PERF | Performance Analysis Example Lab
# setup env variables

MEMCD=$(kubectl get pods -l app=memcd-server -o jsonpath='{.items[0].metadata.name}')
AWING=$(kubectl get pods -l app=a-wing -o jsonpath='{.items[0].metadata.name}')
XWING=$(kubectl get pods -l app=x-wing -o jsonpath='{.items[0].metadata.name}')
TRACKER=$(kubectl get pods -l name=fleet-tracker -o jsonpath='{.items[0].metadata.name}')

echo "MEMCD=$MEMCD"
echo "AWING=$AWING"
echo "XWING=$XWING"
echo "TRACKER=$TRACKER"
