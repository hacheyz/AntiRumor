package cn.edu.hit.backend.service;

import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Question;

import java.util.Map;

public interface QuestionService {
  // 添加提问
  void add(String question);

  PageBean<Question> pagelist(Map<String, Object> map);
}
