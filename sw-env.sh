#/bin/bash
# Jesko Mueller (c) 2021
# ZHAW CCP1-PERF | Performance Analysis Example Lab
# setup env variables

MEMCD_SERVER_POD=$(kubectl get pods -l app=memcd-server -o jsonpath='{.items[0].metadata.name}')
AWING_POD=$(kubectl get pods -l app=a-wing -o jsonpath='{.items[0].metadata.name}')
XWING_POD=$(kubectl get pods -l app=x-wing -o jsonpath='{.items[0].metadata.name}')
TRACKER_POD=$(kubectl get pods -l name=fleet-tracker -o jsonpath='{.items[0].metadata.name}')

echo "MEMCD_SERVER_POD=$MEMCD_SERVER_POD"
echo "AWING_POD=$AWING_POD"
echo "XWING_POD=$XWING_POD"
echo "TRACKER_POD=$TRACKER_POD"
