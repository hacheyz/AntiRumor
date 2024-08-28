package cn.edu.hit.backend.service;

import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Rumor;
import cn.edu.hit.backend.pojo.Tag;

import java.util.List;
import java.util.Map;

public interface RumorService {
  // 分页查询
  PageBean<Rumor> pagelist(Map<String, Object> map);

  List<Tag> getTagsForRumor(Integer rumorId);
}
