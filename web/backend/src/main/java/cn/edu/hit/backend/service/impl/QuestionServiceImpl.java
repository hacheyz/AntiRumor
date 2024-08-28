package cn.edu.hit.backend.service.impl;

import cn.edu.hit.backend.mapper.QuestionMapper;
import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Question;
import cn.edu.hit.backend.service.QuestionService;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;

@Service
public class QuestionServiceImpl implements QuestionService {
  @Autowired
  private QuestionMapper questionMapper;

  @Override
  public void add(String question) {
    LocalDate create_date = LocalDate.now();
    questionMapper.add(question, create_date);
  }

  // 分页查询
  // 支持searchQuestion的模糊查询
  @Override
  public PageBean<Question> pagelist(Map<String, Object> map) {
    PageBean<Question> pb = new PageBean<>();
    Integer pageNum = (Integer) map.get("pageNum");
    Integer pageSize = (Integer) map.get("pageSize");

    String searchQuestion = (String) map.get("searchQuestion");

    PageHelper.startPage(pageNum, pageSize);

    List<Question> as = questionMapper.pagelist(searchQuestion);

    Page<Question> p = (Page<Question>) as;

    pb.setTotal(p.getTotal());
    pb.setItems(p.getResult());
    return pb;
  }
}
