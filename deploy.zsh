#!/usr/bin/zsh

source .env

#docker build $DEV_PATH/elasticsearch \
#-t ${ELASTIC_IMG_NAME} \
#--build-arg ELASTIC_VERSION=${ELASTIC_VERSION}

docker run \
-p 9200:9200 \
-e "ES_JAVA_OPTS=-${MIN_HEAP} -${MIN_HEAP}" \
${ELASTIC_IMG_NAME} 


#-e "discovery.type=single-node" \
#-e "ES_HEAP_SIZE=${HEAP_SIZE}" \
