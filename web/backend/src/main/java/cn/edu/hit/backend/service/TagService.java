package cn.edu.hit.backend.service;

import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Tag;

import java.util.List;
import java.util.Map;

public interface TagService {

  // 根据标签名查找标签
  Tag findByTagName(String name);

  // 添加标签
  void addTag(String name);

  // 分页查询标签
  PageBean<Tag> pagelist(Map<String, Object> map);

  // 获取标签列表(不带relateNum)
  List<Tag> list();

  // 获取标签列表(带relateNum)
  List<Tag> listWithRelateNum();
}
