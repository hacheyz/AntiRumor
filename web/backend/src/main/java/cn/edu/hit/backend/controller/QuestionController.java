package cn.edu.hit.backend.controller;

import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Question;
import cn.edu.hit.backend.pojo.Result;
import cn.edu.hit.backend.service.QuestionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/question")
public class QuestionController {
  @Autowired
  private QuestionService questionService;

  @PostMapping("/add")
  public Result add(String question) {
    questionService.add(question);
    return Result.success("问题添加成功");
  }

  @PostMapping("/pagelist")
  public Result<PageBean<Question>> pagelist(@RequestBody Map<String, Object> map) {
    return Result.success(questionService.pagelist(map));
  }

  @GetMapping("/addAgree")
  public Result addAgree(Integer id) {
    questionService.addAgree(id);
    return Result.success();
  }

  @GetMapping("/addDisagree")
  public Result addDisagree(Integer id) {
    questionService.addDisagree(id);
    return Result.success();
  }
}
