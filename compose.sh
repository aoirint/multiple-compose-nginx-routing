#!/bin/bash
ARTICLE_APP_HOST_ROOT="${PWD}/article-api" \
COMMENT_APP_HOST_ROOT="${PWD}/comment-api" \
docker-compose \
  --project-directory="${PWD}" \
  -f article-api/docker-compose.yml \
  -f comment-api/docker-compose.yml \
  -f ./docker-compose.yml \
  $@
